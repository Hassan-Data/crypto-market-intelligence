
import requests
import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv
from datetime import datetime
print(os.path.exists('config/.env'))  # <-- Should print True

# Load environment variables
load_dotenv(dotenv_path='config/.env')
print("DB_NAME:", os.getenv("DB_NAME"))
print("DB_USER:", os.getenv("DB_USER"))
print("DB_PASS:", os.getenv("DB_PASS"))
print("DB_HOST:", os.getenv("DB_HOST"))
print("CMC_API_KEY:", os.getenv("CMC_API_KEY"))

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
CMC_API_KEY = '53b1139d-5542-41f4-870d-8694df01e70a'


# CoinMarketCap API URL
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': CMC_API_KEY,
}
params = {
    'start': '1',
    'limit': '100',
    'convert': 'USD'
}

# Fetch data
response = requests.get(url, headers=headers, params=params)
data = response.json()['data']

# Convert to DataFrame
df = pd.json_normalize(data)
df = df[[
    'id', 'name', 'symbol', 'slug', 'num_market_pairs', 'date_added', 'max_supply',
    'circulating_supply', 'total_supply', 'cmc_rank', 'last_updated',
    'quote.USD.price', 'quote.USD.volume_24h', 'quote.USD.percent_change_1h',
    'quote.USD.percent_change_24h', 'quote.USD.percent_change_7d',
    'quote.USD.market_cap', 'quote.USD.market_cap_dominance', 'quote.USD.fully_diluted_market_cap'
]]
df.columns = [
    'cmc_id', 'name', 'symbol', 'slug', 'num_market_pairs', 'date_added', 'max_supply',
    'circulating_supply', 'total_supply', 'cmc_rank', 'last_updated',
    'price', 'volume_24h', 'percent_change_1h',
    'percent_change_24h', 'percent_change_7d',
    'market_cap', 'market_cap_dominance', 'fully_diluted_market_cap'
]
df['date_added'] = pd.to_datetime(df['date_added'])
df['last_updated'] = pd.to_datetime(df['last_updated'])

# Database connection
conn = psycopg2.connect(
    dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST
)
cur = conn.cursor()

# Create table if not exists
cur.execute("""
CREATE TABLE IF NOT EXISTS crypto_listings_latest (
    id SERIAL PRIMARY KEY,
    cmc_id INT,
    name TEXT,
    symbol TEXT,
    slug TEXT,
    num_market_pairs INT,
    date_added TIMESTAMP,
    max_supply NUMERIC,
    circulating_supply NUMERIC,
    total_supply NUMERIC,
    cmc_rank INT,
    last_updated TIMESTAMP,
    price NUMERIC,
    volume_24h NUMERIC,
    percent_change_1h NUMERIC,
    percent_change_24h NUMERIC,
    percent_change_7d NUMERIC,
    market_cap NUMERIC,
    market_cap_dominance NUMERIC,
    fully_diluted_market_cap NUMERIC
);
""")
conn.commit()

# Insert data
for index, row in df.iterrows():
    cur.execute("""
        INSERT INTO crypto_listings_latest (
            cmc_id, name, symbol, slug, num_market_pairs, date_added,
            max_supply, circulating_supply, total_supply, cmc_rank, last_updated,
            price, volume_24h, percent_change_1h, percent_change_24h,
            percent_change_7d, market_cap, market_cap_dominance, fully_diluted_market_cap
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, tuple(row))
conn.commit()
conn.close()
print("ETL process completed successfully!")
