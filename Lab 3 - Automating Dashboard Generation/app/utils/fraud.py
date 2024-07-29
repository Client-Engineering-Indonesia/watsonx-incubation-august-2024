import os
import json
import pandas as pd
import ibm_db_dbi as dbi

class InvoiceChecking:
    def __init__(self):
        
        self.wx_api_key = os.environ["WX_API_KEY"]
        self.wx_project_id = os.environ["WX_PROJECT_ID"]
        self.wx_url = os.environ["WX_URL"]
        self.db2_host = os.environ["DB2_HOST"]
        self.db2_port = os.environ["DB2_PORT"]
        self.db2_username = os.environ["DB2_USERNAME"]
        self.db2_password = os.environ["DB2_PASSWORD"]

        self.creds = {
            "url": self.wx_url ,
            "apikey": self.wx_api_key 
        }

    def db2_init(self):
        
        db2_dsn = 'DATABASE={};HOSTNAME={};PORT={};PROTOCOL=TCPIP;UID={uid};PWD={pwd};SECURITY=SSL'.format(
            'bludb',
            self.db2_host,   
            self.db2_port,         
            uid=self.db2_username,     
            pwd=self.db2_password     
        )
        db2_connection = dbi.connect(db2_dsn)
        
        return db2_connection

    def query_db2_df(self, query):
        
        db2_connection = self.db2_init()
        answer_df = pd.read_sql_query(query, con=db2_connection)
        
        return answer_df

    def get_database_items(self, table_name):
        
        query_init = f"SELECT * FROM {table_name}"
        answer_df = self.query_db2_df(query_init)
        json_database = answer_df.to_json(orient='records', lines=True)
        
        return self.parse_json_database(json_database)

    def parse_json_database(self, json_str):
        
        items = []
        for line in json_str.strip().splitlines():
            item = json.loads(line)
            items.append(item)
            
        return items

    def check_items(self, json_input, database_items):
        
        results = []
        for item in json_input:
            product_name = item['Nama Produk']
            harga_produk = item['Harga Produk']
            jumlah = int(item['Jumlah'])  # Convert Jumlah to int
            total_harga = item['Total Harga']

            # Find the corresponding item in database_items
            matched_item = next((prod for prod in database_items if prod['NAMA'] == product_name), None)

            if matched_item:
                db_harga = matched_item['HARGA']
                db_total_harga = db_harga * jumlah  # Calculate total price from database price

                harga_match = harga_produk == db_harga
                total_harga_match = total_harga == db_total_harga

                if harga_match and total_harga_match:
                    status = 'Match'
                    message = f"Produk '{product_name}' sudah sesuai dengan database dimana harga produk 'Rp{harga_produk}' dengan jumlah sebanyak '{jumlah}' sebesar Rp'{db_total_harga}'"
                elif harga_match:
                    status = 'Partial Match'
                    message = f"Produk '{product_name}' sudah sesuai dengan database dimana harga produk 'Rp{harga_produk}', akan tetapi apabila jumlah sebanyak '{jumlah}' seharusnya 'Rp{db_total_harga}' bukan 'Rp{total_harga}'"
                elif total_harga_match:
                    status = 'Partial Match'
                    message = f"Produk '{product_name}' sudah sesuai dengan database dimana harga total harga sebesar 'Rp{db_total_harga}' dengan jumlah sebanyak '{jumlah}' namun ada kesalahan input pada harga senilai 'Rp{harga_produk}' melainkan 'Rp{db_harga}'"
                else:
                    status = 'Mismatch'
                    message = f"Produk '{product_name}' tidak sesuai dengan harga atau total harga yang benar."
            else:
                status = 'Not Found'
                message = f"Item '{product_name}' tidak ditemukan dalam database."

            results.append({'Produk': product_name, 'Status': status, 'Message': message})

        return results

    def validate_products(self, json_upload, table_name):
        print(json_upload)
        json_input = json_upload["NOTA SALES"]["Produk"]
        database_items = self.get_database_items(table_name)
        results = self.check_items(json_input, database_items)
        print(results)
        return json.loads(json.dumps(results))
