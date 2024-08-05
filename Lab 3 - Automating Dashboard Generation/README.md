# Building Text2SQL application with watsonx.ai
Repository ini berisikan code dari sebuah webapp yang menggunakan Flask python sebagai backend dan Vanilla Java Script, HTML, CSS sebagai Front-end.
Front-end juga menggukan open source HTML web component yang dibuat oleh IBM, dinamakan [Carbon](https://web-components.carbondesignsystem.com/?path=/docs/introduction-welcome--page).

Aplikasi ini memungkinkan Anda melakukan tanya jawab menggunakan data yang ada di-database dengan bantuan LLM Model. Hal yang biasanya Anda tanyakan ke data analyst, sekarang dapat Anda tanyakan secara mandiri ke app ini. Metode yang digunakan untuk melakukannya dinamakan [Text to SQL](https://research.ibm.com/blog/granite-LLM-text-to-SQL). Dimana pertanyaan dari pengguna diubah menjadi SQL query oleh LLM Model dan SQL query ini akan digunakan untuk mendapatkan data dari DB. Setelah data didapatkan, LLM pula yang akan menjawab pertanyaan Anda menjadi jawaban yang mudah dipahami.


Coba secara langsung applikasi yang sudah di deploy [disini](https://ibmjaya.1jk7wywevfmh.us-south.codeengine.appdomain.cloud/)

## How this app works? 🚀
Aplikasi ini memungkinkan pengguna melakukan tanya jawab dengan LLM seputar data penjualan yang ada di database. Berikut adalah kapabilitas dari aplikasi ini: 
1. Pengguna dapat melakukan tanya jawab seputar data penjualan. Jika data dirasa cocok, LLM juga akan men-generate chart sebagai jawaban anda.
2. Tambahan di Tab ke-2 dimana contoh Fraud detection atau mismatch saat input data dapat dilakukan.

### Contoh Pertanyaan yang bisa ditanyakan
Berikut adalah contoh-contoh pertanyaan apakah aplikasi berjalan dengan semestinya.
- Tampilkan top 5 produk dengan total penjualan terbanyak
- Tampilkan top 5 salesman dengan total penjualan tertinggi
- Tampilkan 5 daerah dengan penjualan terbanyak
- Kapan paling lambat customer toko ismail bayar invoicenya?
- Siapa saja yang disupervisi oleh Jupri?
- Kapan paling lambat customer id 340362 bayar invoicenya?
- Berapa yang harus dibayar oleh customer dua sultan dan berapa yang tersisa?


## Requirements 🚀
### Teknologi yang digunakan
Untuk membangun webapp ini beberapa SDK digunakan untuk memungkinkan interaksi dengan teknologi atau service yang diperlukan.
1. [watsonx.ai python SDK](https://ibm.github.io/watsonx-ai-python-sdk/)
2. [DB2](https://www.ibm.com/docs/en/db2/11.5?topic=framework-application-development-db)


Selain menggunakan SDK, kita sebenarnya juga bisa menggunakan API. Berikut adalah link dokumentasi untuk beberapa API yang mungkin berguna untuk anda.
- [watsonx.ai API Documentation](https://cloud.ibm.com/apidocs/watsonx-ai)
- [Watson Discovery API Documentation](https://www.ibm.com/docs/en/db2/11.5?topic=apis-administrative)
  
### Credentials yang harus di sediakan
Agar web application ini dapat dijalankan dengan baik di local computer ataupun di docker container anda harus menyiapkan credentials dan secret berikut.
- watsonx.ai APIKEY
- watsonx.ai PROJECT_ID
- watsonx.ai URL
- DB2 HOST 
- DB2 DB2 PORT
- DB2 USERNAME
- DB2 PASSWORD
  
## Cara memulai 🚀
Ada beberapa cara untuk mendeploy code yang ada di repository ini untuk menjadi sebuah webapp yang dapat dioperasikan.
Pertama, anda bisa menjalankan code tersebut di local computer anda. Cara kedua, anda bisa mendeploynya dengan Docker Container. 
Penggunakan Docker container menguntungkan karena dapat di-deploy dimana saja dengan mudah.
  
### Running di Local Computer
1. Buka terminal, cd kedalam directory Lab 4.
2. create python virtual environment, berikut adalah contoh jika anda ingin membuat virtual environment bernama 'genai'  
```
python -m venv genai
```  

3. aktifkan python virtual environment yang baru saja dibuat  
```
source genai\bin\activate
```  

4. install dependencies yang ada di requirements.txt  
```
python -m pip install -r requirements.txt
```  

5. export secret dan credentials dengan mengganti semua value yang ada didalam double quote dengan credentials anda. Paste command tersebut di terminal.  
```
export WX_API_KEY="IAM-APIKEY"
export WX_PROJECT_ID="WATSONXAI-PROJECT-ID"
export WX_URL="WATSONXAI-URL"
export DB2_HOST="DB2-HOST"
export DB2_PORT="DB2-PORT"
export DB2_USERNAME="DB2-USERNAME"
export DB2_PASSWORD="DB2-PASSWORD"
```    

6. cd ke folder app dan jalankan aplikasi  
```
cd app
python main.py
```  
7. Buka local `127.0.0.0:8080` atau IP yang muncul di terminal setelah applikasi dijalankan.
  
  
### Running menggunakan Docker Container

1. Buka terminal, cd kedalam directory Lab 4.
2. Build docker image menggunakan docker file  
```
docker build -t text2sql .
```  
3. Run docker container dengan menjadikan credentials dan secret sebagai environment variable.
```
docker run --env "WX_API_KEY=IAM-APIKEY" \
--env "WX_PROJECT_ID=WATSONXAI-PROJECT-ID" \
--env "WX_URL=WATSONXAI-URL" \
--env "DB2_HOST=DB2-HOST" \
--env "DB2_PORT=DB2-PORT" \
--env "DB2_USERNAME=DB2-USERNAME" \
--env "DB2_PASSWORD=DB2-PASSWORD" \
-p 8080:8080 --name text2sql-container text2sql
```  
4. Buka URL deployment.

