@echo off
cd /d C:\Users\hassa\OneDrive\Documents\EU\Business Intelligence\ETL Project\crypto_listings_etl_project

:: Activate the virtual environment
call venv\Scripts\activate.bat

:: Run ETL and log output with timestamp
echo ------------------------------ >> etl_logs\etl_log.txt
echo [%date% %time%] Running ETL... >> etl_logs\etl_log.txt
python scripts\etl_crypto_listings.py >> etl_logs\etl_log.txt 2>&1
echo [%date% %time%] Finished ETL >> etl_logs\etl_log.txt
