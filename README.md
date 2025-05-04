# Stock Sentiment Analyzer

A tool that pulls Reddit discussions on a given stock ticker, analyzes sentiment using TextBlob, and visualizes results alongside real‐time price data from Yahoo Finance. Includes both a command‑line interface, a Flask web app, and an interactive Streamlit dashboard.

---

## 🚀 Features

* **Reddit Sentiment Analysis**: Fetches posts from r/stocks, r/investing, and r/wallstreetbets.
* **TextBlob Polarity Scoring**: Cleans and scores post titles & bodies for positive/negative sentiment.
* **Price Data Fetching**: Retrieves current price (and currency) and historical close prices via yfinance.
* **Multiple Interfaces**:

  * **CLI**: Quick `python stock_sentiment.py [TICKER]`
  * **Flask Web App**: Self‑hosted at `http://localhost:5000/`
  * **Streamlit Dashboard**: Interactive dashboard with charts and expanders.
* **Robust Fetching**: Retry logic to handle transient errors or API rate‑limits.

---

## 📋 Requirements

* Python 3.8+
* Reddit developer account (client ID & secret)
* A free Yahoo Finance API access via yfinance

Dependencies are listed in `requirements.txt`:

```bash
praw
python-dotenv
textblob
pandas
yfinance
Flask
streamlit
```

---

## 🔧 Installation

1. **Clone the repo**

   ```bash
   ```

git clone [https://github.com/shashanks33/stock-sentiment-analyzer.git](https://github.com/shashanks33/stock-sentiment-analyzer.git)
cd stock-sentiment-analyzer

````

2. **Create & activate a virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate     # macOS/Linux
./venv/Scripts/Activate.ps1  # Windows PowerShell
````

3. **Install dependencies**

   ```bash
   ```

pip install -r requirements.txt

````

4. **Configure credentials**
- Copy `.env.example` to `.env` and fill in your Reddit credentials:
  ```ini
REDDIT_CLIENT_ID=your_id_here
REDDIT_CLIENT_SECRET=your_secret_here
REDDIT_USER_AGENT=desktop:StockSentiment:v1.0 (by /u/your_username)
  ```

---

## ⚙️ Usage

### 1. Command‑Line Interface

```bash
# Run with a symbol and optional limit:
python stock_sentiment.py AAPL 50
````

* Fetches latest 50 posts, prints each compound score, average sentiment, verdict, and last month’s price range.

### 2. Flask Web App

```bash
export FLASK_APP=src/app.py
export FLASK_ENV=development    # optional: for auto‑reload + debug logs
flask run
```

Open your browser at `http://127.0.0.1:5000/`, enter a ticker, and click **Analyze**.

### 3. Streamlit Dashboard

```bash
streamlit run src/streamlit_app.py
```

This launches an interactive UI with real‑time charts, metrics, and expandable Reddit posts.

---

## 📂 Project Structure

```
.
├── stock_sentiment.py       # CLI prototype
├── requirements.txt         # Python deps
├── .env                     # your Reddit creds (gitignored)
├── src/
│   ├── app.py               # Flask routes + templates
│   ├── reddit_sentiment.py  # TextBlob + PRAW wrapper class
│   ├── stock_data.py        # yfinance wrapper with retry logic
│   ├── streamlit_app.py     # Streamlit front‑end
│   └── templates/           # Jinja2 HTML templates
└── visualization/           # placeholder for custom charts
```

---

## 💡 Extensions & Ideas

* Swap TextBlob for a transformer‑based sentiment model (e.g. Hugging Face).
* Replace threshold logic with a trained classifier. Drop the model under `src/models/`.
* Add caching (Redis) to avoid rate‑limits and speed up repeat queries.
* Enhance the front end with Bootstrap/Tailwind or a React dashboard.

---

## 🤝 Contributing

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/foo`)
3. Commit your changes (`git commit -am 'Add foo'`)
4. Push to branch (`git push origin feature/foo`)
5. Open a Pull Request

Please follow the [Contributor Covenant](https://www.contributor-covenant.org/) code of conduct.

---

## 📝 License

This project is released under the MIT License. See `LICENSE` for details.
