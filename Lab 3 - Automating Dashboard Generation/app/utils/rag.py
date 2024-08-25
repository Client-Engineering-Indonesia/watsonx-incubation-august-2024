import sys
import json
import requests
import ast, os
import pandas as pd
import time
import ibm_db, ibm_db_dbi as dbi

from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams

#Creds related to watsonx.ai
WX_API_KEY = os.environ["WX_API_KEY"]
WX_PROJECT_ID = os.environ["WX_PROJECT_ID"]
WX_URL = os.environ["WX_URL"]

DB2_HOST = os.environ["DB2_HOST"]
DB2_PORT = os.environ["DB2_PORT"]
DB2_USERNAME = os.environ["DB2_USERNAME"]
DB2_PASSWORD = os.environ["DB2_PASSWORD"]


creds = {
    "url": WX_URL,
    "apikey": WX_API_KEY 
}

#=============================DB2 Function==============================
def db2_init(DB2_HOST=DB2_HOST, DB2_PORT=DB2_PORT, DB2_USERNAME=DB2_USERNAME, DB2_PASSWORD=DB2_PASSWORD):
    db2_dsn = 'DATABASE={};HOSTNAME={};PORT={};PROTOCOL=TCPIP;UID={uid};PWD={pwd};SECURITY=SSL'.format(
        'bludb',
        DB2_HOST,   
        DB2_PORT,         
        uid=DB2_USERNAME,     
        pwd=DB2_PASSWORD     
    )

    db2_connection = dbi.connect(db2_dsn)
    return db2_connection

db2_connection = db2_init()

def query_db2_df(query, db2_connection = db2_connection):    
    answer_df = pd.read_sql_query(query, con=db2_connection)
    db2_connection.close()
    return answer_df

#=============================Get from main table==============================
table_name = "SCHEMA.SALESMAIN"
query_init = f"SELECT * FROM {table_name}"
answer_df = query_db2_df(query_init)
header = list(answer_df.columns)

#==================================watsonx.ai===================================== 
def send_to_watsonxai(prompt, creds=creds, project_id=WX_PROJECT_ID,
                    model_name= 'meta-llama/llama-3-8b-instruct',#'meta-llama/llama-3-70b-instruct', #'mistralai/mixtral-8x7b-instruct-v01',', #'meta-llama/llama-2-13b-chat', #
                    decoding_method="greedy",
                    max_new_tokens=300,
                    min_new_tokens=1,
                    temperature=0,
                    repetition_penalty=1.0,
                    stop_sequences=["\n","\n\n"],
                    ):
    '''
   helper function for sending prompts and params to Watsonx.ai
    
    Args:  
        prompts:list list of text prompts
        decoding:str Watsonx.ai parameter "sample" or "greedy"
        max_new_tok:int Watsonx.ai parameter for max new tokens/response returned
        temperature:float Watsonx.ai parameter for temperature (range 0>2)
        repetition_penalty:float Watsonx.ai parameter for repetition penalty (range 1.0 to 2.0)

    Returns: None
        prints response
    '''

    assert not any(map(lambda prompt: len(prompt) < 1, prompt)), "make sure none of the prompts in the inputs prompts are empty"

    # Instantiate parameters for text generation
    model_params = {
        GenParams.DECODING_METHOD: decoding_method,
        GenParams.MIN_NEW_TOKENS: min_new_tokens,
        GenParams.MAX_NEW_TOKENS: max_new_tokens,
        GenParams.RANDOM_SEED: 42,
        GenParams.TEMPERATURE: temperature,
        GenParams.REPETITION_PENALTY: repetition_penalty,
        GenParams.STOP_SEQUENCES: stop_sequences
    }

    # Instantiate a model proxy object to send your requests
    model = Model(
        model_id=model_name,
        params=model_params,
        credentials=creds,
        project_id=project_id)
    
    
    output = model.generate_text(prompt)
    return output


def send_to_watsonxai_stream(prompt, creds=creds, project_id=WX_PROJECT_ID,
                    model_name= 'meta-llama/llama-3-8b-instruct',#'meta-llama/llama-3-70b-instruct', #'mistralai/mixtral-8x7b-instruct-v01',', #'meta-llama/llama-2-13b-chat', #
                    decoding_method="greedy",
                    max_new_tokens=300,
                    min_new_tokens=1,
                    temperature=0,
                    repetition_penalty=1.0,
                    stop_sequences=["\n","\n\n"],
                    ):
    '''
   helper function for sending prompts and params to Watsonx.ai
    
    Args:  
        prompts:list list of text prompts
        decoding:str Watsonx.ai parameter "sample" or "greedy"
        max_new_tok:int Watsonx.ai parameter for max new tokens/response returned
        temperature:float Watsonx.ai parameter for temperature (range 0>2)
        repetition_penalty:float Watsonx.ai parameter for repetition penalty (range 1.0 to 2.0)

    Returns: None
        prints response
    '''

    assert not any(map(lambda prompt: len(prompt) < 1, prompt)), "make sure none of the prompts in the inputs prompts are empty"

    # Instantiate parameters for text generation
    model_params = {
        GenParams.DECODING_METHOD: decoding_method,
        GenParams.MIN_NEW_TOKENS: min_new_tokens,
        GenParams.MAX_NEW_TOKENS: max_new_tokens,
        GenParams.RANDOM_SEED: 42,
        GenParams.TEMPERATURE: temperature,
        GenParams.REPETITION_PENALTY: repetition_penalty,
        GenParams.STOP_SEQUENCES: stop_sequences
    }

    # Instantiate a model proxy object to send your requests
    model = Model(
        model_id=model_name,
        params=model_params,
        credentials=creds,
        project_id=project_id)
    
    output = model.generate_text_stream(prompt)

    for chunk in output:
        yield chunk
        
   

def question_to_sql(user_question, table_name=table_name,header=header):
    prompt_query = f"""
        Anda adalah asisten yang bertugas untuk mengkonversi pertanyaan ke dalam bentuk SQL. Buatlah kueri SQL berdasarkan dari 2 tabel informasi beserta kolom pada "table_schema" untuk menjawab pertanyaan dalam bentuk format JSON.

        table_schema: 
        table: {table_name}
        columns: {header}
        
        Informasi penting:
        - Kolom yang difilter tampilkan juga pada list kolom
        - Setiap menampilkan kolom Salesman atau customer atau invoice atau supervisor harus menampilkan juga kolom Location
        - Setiap menampilkan kolom Invoice sertakan juga informasi customer dan lokasi
        - Tampilkan informasi sesuai yang ditanyakan, tidak perlu melakukan relasi ke table yang tidak ditanyakan
        - Istilah Cabang berarti Plant dan Stockpoint berarti Salespoint. Atau sebaliknya
        - Pertanyaan yang terkait nama lokasi, nama salespoint, nama plant, nama cabang gunakan filter WHERE LIKE '%'. Jika nilai dari nama mengandung spasi, maka berikan filter dengan memberikan spasi dan tanpa spasi
        - Pada table ProductMaster tidak perlu lakukan link join kolom LocationID
        - Kolom yang difilter tampilkan juga pada list kolom
        - Setiap menampilkan kolom Salesman atau customer atau invoice atau supervisor harus menampilkan juga kolom Location
        - Istilah Cabang berarti Plant dan Sockpoint berarti Salespoint. Atau sebaliknya
        - Pertanyaan yang terkait nama lokasi, nama salespoint, nama plant, nama cabang gunakan filter WHERE LIKE '%'. Jika nilai dari nama mengandung spasi, maka berikan filter dengan memberikan spasi dan tanpa spasi

        Contoh pertanyaan dan kueri SQL:

        Pertanyaan: Tampilkan top 5 salesman dengan total penjualan tertinggi
        Jawaban: {{"query": "SELECT SALESMANNAME, SALESMANCITY, SUM(NETSALESAMOUNT) AS TotalSalesAmount FROM SCHEMA.SALESMAIN GROUP BY SALESMANNAME, SALESMANCITY ORDER BY TotalSalesAmount DESC LIMIT 5;"}}

        Pertanyaan: Tampilkan customer yang berada di kota Bogor
        Jawaban: {{"query": "SELECT DISTINCT CUSTOMERNAME, CUSTOMERPHONE, CUSTOMERGROUP, CUSTOMERADDRESS, CUSTOMERCOUNTRY, CUSTOMERTYPE FROM SCHEMA.SALESMAIN WHERE UPPER(CUSTOMERCITY) = UPPER('Bogor');"}}

        Pertanyaan: Perusahaan ABC ada di kota apa saja?
        Jawaban: {{"query": "SELECT DISTINCT COMPANYNAME, CITY FROM SCHEMA.SALESMAIN WHERE COMPANYNAME = 'PT. ABC';"}}

        Pertanyaan: Tampilkan top 5 produk dengan total penjualan terbanyak
        Jawaban: {{"query": "SELECT PRODUCTID, SHORTNAME, SUM(NETSALESQUANTITY) AS TotalSalesQuantity FROM SCHEMA.SALESMAIN GROUP BY PRODUCTID, SHORTNAME ORDER BY TotalSalesQuantity DESC LIMIT 5;"}}
        
        Pertanyaan:"Kapan paling lambat customer toko ismail bayar invoicenya?"
        Jawaban: {{"query": "SELECT MAX(DUEDATE) AS LatestDueDate FROM SCHEMA.SALESMAIN WHERE LOWER(CUSTOMERNAME) LIKE LOWER('%TOKO ismail%');"}}

        Pertanyaan: Berapa yang harus dibayar oleh customer dua sultan dan berapa yang tersisa?
        Jawaban: {{"query": "SELECT SUM(LASTAMOUNT) AS TotalAmountToPay, SUM(LASTAMOUNT - PAYMENTAMOUNT) AS RemainingAmount FROM SCHEMA.SALESMAIN WHERE LOWER(CUSTOMERNAME) LIKE LOWER('%dua sultan%');"}}
        
        Pertanyaan: Siapa saja yang disupervisi oleh Jupri?
        Jawaban: {{"query": "SELECT DISTINCT SALESMANNAME FROM SCHEMA.SALESMAIN WHERE LOWER(SUPERVISORNAME) LIKE LOWER('%Jupri%');"}}
        
        Pertanyaan: Tampilkan salesman di Surabaya?
        Jawaban: {{"query": "SELECT DISTINCT SALESMANNAME, SALESMANCITY, SALESMANPHONE, SALESMANSTATUS FROM SCHEMA.SALESMAIN WHERE LOWER(SALESMANCITY) = LOWER('Surabaya');"}}
                
        Pertanyaan: {user_question}
        Jawaban:
        """

    try:
        query = send_to_watsonxai(prompt_query, model_name='meta-llama/llama-3-8b-instruct', min_new_tokens=2,
                                           max_new_tokens=300, stop_sequences=["\n\n", "}"])
        print(f"{query}\n")
        query = query.strip().split("\n")[0]
        query = ast.literal_eval(query)['query']
            
    except:
        return "error: can't generate SQL queries properly"
    
    try:
        query_result = query_db2_df(query)
        data = query_result.to_dict(orient="records")
        print(f"{data}\n")
        
        prompt_visual = f"""
            Anda sebagai asisten harus menentukan apakah json "json_query" berikut dapat divisualisasikan dalam bentuk histogram.

            json_query: {data}

            Jawaban harus berupa string "True" jika dapat divisualisasikan dalam bentuk histogram atau string "False" jika tidak bisa.
            Syarat untuk histogram adalah apabila informasinya dapat readable dengan data point lebih dari 3 data point dan tentukan "x-axis" dan "y-axis" untuk visualisasi apabila chart sama dengan "True"
            Tuliskan jawaban dalam format JSON: '{{"chart": "True atau False", "x": "x-axis", "y": y-axis}}'. 

            Jawaban:
            """

        output_visual = send_to_watsonxai(prompt_visual, model_name='mistralai/mixtral-8x7b-instruct-v01', min_new_tokens=8,
                                    max_new_tokens=300, stop_sequences=["\n\n", "}"])
        
        parsed_visual = json.loads(output_visual)
        output_visual = json.dumps(parsed_visual, indent=0).strip().replace('\n', '')
        print(f"{output_visual}\n")
        
        return {"output": data, "visual": ast.literal_eval(output_visual)}
    
    except:
        return []
    

def query_wxai(user_question, data, streaming=False):
    print(user_question)
    start_time = time.time()

    if data ==[]:
        print("NO DATA")
        return {'answer': "Maaf, informasi yang anda butuhkan tidak tersedia di database, silahkan coba dengan pertanyaan lain! Terima kasih."}
    else:
        prompt = f"""
            Anda adalah customer service dari perusahaan Penjualan yang bertugas untuk menjawab semua pertanyaan terkait data Sales, data Piutang, dan data Pembayaran.
            Tugas Anda adalah untuk memberikan jawaban yang baik, ramah, dan menarik berdasarkan pertanyaan user_question dan hasil query_result yang diberikan.

            user_question: {user_question}
            query_result: {data}
    
            Instruksi analisa:
            1. Jika query_result mengalami error, jawablah dengan sopan bahwa Anda tidak bisa menjawabnya.
            2. Jangan menjawab pertanyaan apapun apabila Anda tidak tahu jawabannya.
            3. Apabila pertanyaan mengandung jumlah besaran angka, formatlah angka tersebut sebagai uang dengan menggunakan desimal dan standar rupiah.
            4. Jika jawaban ditulis dengan huruf kapital semua, ubah menjadi format yang mengikuti kaidah bahasa Indonesia.
            5. Jika tidak bisa menjawab pertanyaan user dengan benar, maka jawablah dengan 'Maaf informasi yang ada tidak cukup untuk menjawab pertanyaan anda'.
            6. Hindari penggunaan baris baru saat menjawab.
            7. Jawablah pertanyaanya menjadi menjadi suatu kalimat yang menjelaskan query_result
            8. Jangan menambahkan informasi apapun selain penjelasan terkait "query_result"

            Jawaban:"""
        
    print("streaming =", streaming)

    if streaming:
        return send_to_watsonxai_stream(prompt, creds=creds, project_id=WX_PROJECT_ID, model_name='meta-llama/llama-3-70b-instruct', min_new_tokens=8,
                                            max_new_tokens=300, stop_sequences=["\n\n", "}"])

    else:
        result = send_to_watsonxai(prompt, creds=creds, project_id=WX_PROJECT_ID, model_name='meta-llama/llama-3-70b-instruct', min_new_tokens=8,
                                            max_new_tokens=300, stop_sequences=["\n\n", "}"])
        eta_wx = time.time() - start_time
        print("eta_wx: ", eta_wx)
        return result, eta_wx
         



    