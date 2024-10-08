import pandas as pd
import mysql.connector


host = 'localhost'
user = 'root'
password = 'root'
database = 'cci'
auth_plugin = 'mysql_native_password'



connection = mysql.connector.connect(
    host = host,
    user = user,
    password = password,
    database = database,
    auth_plugin = auth_plugin
)


cursor = connection.cursor()


def insert_excel_data_to_mysql(final_excel_sheets_path, cursor):
    try:
        df = pd.read_excel(final_excel_sheets_path)

        table_name = "cci_anti_profiteering_orders"
        source_name = "cci_anti_profiteering_orders"
        
        df = df.where(pd.notnull(df), None)
        
        
      
        for index, row in df.iterrows():
            insert_query = f"""
                INSERT INTO {table_name} (source_name, final_orders, link, pdf_name, pdf_path)
                VALUES (%s, %s, %s, %s, %s)
            """
           
            values = (source_name,row["final_orders"], row["link"], row["pdf_name"], row["destination_path"])

         
            cursor.execute(insert_query, values)
        connection.commit()
        cursor.close()
    except Exception as e:
        print(e)


final_excel_sheets_path = r"C:\Users\mohan.7482\Desktop\common functions\cci_anti_historical_updated.xlsx"
insert_excel_data_to_mysql(final_excel_sheets_path, cursor)