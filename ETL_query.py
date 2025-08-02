import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
def query_data():
    try:
        connection = psycopg2.connect(host="localhost",database="retail_sales_db",user="postgres",password="1914")
        query = """ select product,sum(quantity) as total_qty, sum(revenue) as total_revenue from sales_data group by product order by total_revenue DESC;"""
        df = pd.read_sql_query(query,connection)
        print("Product Sales Summary:")
        print(df)
    except Exception as e:
        print("Error:",e)
    finally:
        if connection:
            connection.close()

    df.plot(kind='bar', x='product',y='total_revenue',legend=False)
    plt.title("Revenue by Product")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    query_data()
   