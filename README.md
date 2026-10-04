#  AlphaLeak: Quantitative Analytics Engine

An automated quantitative data pipeline and visualization dashboard for mutual fund performance and risk analytics. 

AlphaLeak is designed to fetch historical Net Asset Value (NAV) data via external APIs, process the time-series data using vectorized mathematics, and calculate institutional-grade risk metrics for financial portfolios.

##  Architecture & Tech Stack
* **Data Ingestion:** `requests` (Handles external API communication and JSON parsing)
* **Data Processing Engine:** `pandas`, `numpy` (Vectorized time-series analysis, datetime indexing, rolling window calculations)
* **Frontend / Dashboard:** `streamlit` (Interactive, web-based UI for real-time querying)

##  Core Financial Analytics
The engine computes several key performance indicators (KPIs) standard in quantitative finance:
* **Maximum Drawdown:** Calculates the maximum observed loss from a historical peak to a trough before a new peak is attained, effectively measuring downside risk.
* **Daily Volatility:** Measures the standard deviation of daily returns to assess the fund's risk profile.
* **Win Rate:** The percentage of trading days where the fund generated a positive return.
* **Cumulative Return & Best/Worst Days:** Absolute performance metrics isolated by specific dates.

##  Edge-Case Resilience
The backend pipeline (`analytics.py`) is engineered to handle common real-world data anomalies:
* Automatically traps and filters out `0` or negative NAV entries to prevent division-by-zero errors.
* Cleanses infinite values (`inf`, `-inf`) resulting from broken data streams, replacing them with structured `NaN` or `0.0` fallbacks.
* Enforces strict chronological sorting and datetime formatting prior to percentage-change calculations.

##  How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/kumarshourya465/ALPHALEAK.git](https://github.com/kumarshourya465/ALPHALEAK.git)
   cd ALPHALEAK

2.  Install dependencies:
    pip install -r requirements.txt

3.  launch the dashboard:
    streamlit run app.py