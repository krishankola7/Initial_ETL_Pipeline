import pandas as pd
from sqlalchemy import create_engine
from config import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME
import urllib.parse



user = urllib.parse.quote_plus(DB_USER)
password = urllib.parse.quote_plus(DB_PASSWORD)


def extract_data(url):
    print("Extracting the data")
    df = pd.read_csv(url)
    return df

def transform_data(df):
    print("Cleaning data")
    df.dropna(inplace=True)
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    return df

def load_data(df, table_name):
    print("Loading the data to MySQL..")
    engine = create_engine(f"mysql+pymysql://{user}:{password}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)
    print("Data loaded successfully")

if __name__ == "__main__":
    DATA_URL = r"C:\Users\Krish Ankola\Downloads\Unilever_Supply_Chain_with_Emissions.csv"
    TABLE_NAME = "unilever_table"

    raw_data = extract_data(DATA_URL)
    clean_data = transform_data(raw_data)
    load_data(clean_data, TABLE_NAME)
