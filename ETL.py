import pandas as pd
def extract():
    df=pd.read_csv('/Users/pranithapadala/Desktop/data-engineering/project01-RetailSalesETL/sales_data.csv')
    return df
def transform(df):
    df=df.dropna()
    df['Price']=df['Price'].astype(float)
    df['Revenue']=df['Quantity']*df['Price']
    return df
def load(df):
    print("Top three columns with max revenue after cleaning and transforming")
    print(df.nlargest(3,'Revenue'))
if __name__ == "__main__":
    df=extract()
    clean_df=transform(df)
    load(clean_df)