# 📊 Crypto Market Intelligence Dashboard  
*A Real-Time BI Project Using Python, PostgreSQL & Power BI*

![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-blue)
![Power BI](https://img.shields.io/badge/Power--BI-Dashboard-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🚀 Overview

This project showcases a real-time Business Intelligence pipeline for the cryptocurrency market. It uses the **CoinMarketCap API** to pull live data, a **Python ETL script** to process it, stores the results in a **PostgreSQL** database, and visualizes them using **Power BI**.

---

## 🧰 Tech Stack

| Tool          | Purpose                            |
|---------------|-------------------------------------|
| Python        | ETL Script (`requests`, `pandas`)  |
| PostgreSQL    | Data Storage                        |
| Power BI      | Dashboard Visualizations            |
| Task Scheduler| Automation                          |

---

## 📂 Folder Structure

```
crypto-market-intelligence/
├── config/                  # .env file (API + DB settings)
├── scripts/                 # ETL script
├── powerbi/                 # Power BI dashboard (.pbix)
├── etl_logs/                # Auto-generated logs
├── run_etl.bat              # Batch script for automation
├── requirements.txt         # Python dependencies
├── .gitignore
├── README.md
└── LICENSE
```

---

## ⚙️ ETL Process

1. **Extract** live market data from [CoinMarketCap API](https://pro.coinmarketcap.com/)
2. **Transform** it using pandas (e.g., clean, select fields)
3. **Load** it into a PostgreSQL table called `crypto_listings_latest`

```python
response = requests.get(api_url, headers=headers, params=params)
data = response.json()['data']
# transform, connect to DB, insert rows...
```

> ✅ See full code: `scripts/etl_crypto_listings.py`

---

## 📊 Power BI Dashboard Highlights

📍 *Screenshot below from actual dashboard*

![Dashboard Preview](./powerbi/dashboard-screenshot.png)

**Visualizations Include:**
- 🔝 Bar chart: Top 10 coins by Market Cap
- 🧁 Donut chart: Market Dominance
- 💡 KPI Cards: Total Volume, Average % Change, Top Coin
- 📋 Conditional table: Price & % changes  
   ➕ Green = Gain, ➖ Red = Loss, ⚪ Gray = No change

---

## 📈 Key Insights
- **BTC + ETH** dominate over 60% of total market cap
- **Volatility** is common among altcoins with low volume
- **Price does not always correlate** with trading volume

---

## ⚡ Setup & Usage

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/crypto-market-intelligence.git
   cd crypto-market-intelligence
   ```

2. Create `.env` in `config/`:
   ```env
   CMC_API_KEY=your_api_key
   DB_NAME=crypto
   DB_USER=postgres
   DB_PASS=your_password
   DB_HOST=localhost
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the ETL:
   ```bash
   python scripts/etl_crypto_listings.py
   ```

5. Or automate it with:
   ```bash
   run_etl.bat
   ```

---

## 🔁 Automation
- Task Scheduler is used to run `run_etl.bat` daily.
- Logs saved to `/etl_logs/etl_log.txt`.

---

## 📈 Future Enhancements

- 🔮 Add ML-based trend prediction (e.g., price forecasting)
- ☁️ Host the dashboard on Power BI Cloud
- 📬 Add Telegram/email alerts on large market movements

---

## 🧑‍💻 Author
**Hassan Noureldin**  
EU Business School — Master's in Business Analytics & Data Science  
📬 [LinkedIn](https://www.linkedin.com/in/yourprofile/)

---

## 📄 License
[MIT](./LICENSE) — use freely, credit appreciated.
