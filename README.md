
# Crypto Listings ETL Project

## Architecture
1. Extract latest cryptocurrency market data from CoinMarketCap API.
2. Transform and clean the data with Pandas.
3. Load the data into PostgreSQL database.
4. Automate the pipeline using a scheduler like cron or Airflow.

## Files
- `scripts/etl_crypto_listings.py`: Main ETL script.
- `config/.env`: Environment variables for database and API key.
- `requirements.txt`: Python dependencies.
