import pandas as pd
import psycopg2 
def extract():
    df=pd.read_csv('/Users/pranithapadala/Desktop/data-engineering/project01-RetailSalesETL/sales_data.csv')
    return df
def transform(df):
    df=df.dropna().copy()
    df['Price']=df['Price'].astype(float)
    df['Revenue']=df['Quantity']*df['Price']
    return df
def load(df):
    try:
        connection = psycopg2.connect(host="localhost",database="retail_sales_db",user="postgres",password="1914")
        cursor = connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS sales_data(product TEXT,quantity INT, price FLOAT, revenue FLOAT);""")
        for _,row in df.iterrows():
            cursor.execute("""INSERT INTO sales_data(product,quantity,price,revenue) VALUES (%s,%s,%s,%s);
                           """,(row['Product'],row['Quantity'],row['Price'],row['Revenue']))
        connection.commit()
        print("Data loaded into postgreSQL successfully.")
    except Exception as e:
        print("Error:",e)
    finally:
        if connection:
            cursor.close()
            connection.close()
if __name__ == "__main__":
    df = extract()
    clean_df=transform(df)
    load(clean_df)