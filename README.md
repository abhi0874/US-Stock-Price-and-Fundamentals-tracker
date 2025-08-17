# 📈 US Stock Price Tracker

A Flask-based web application that provides real-time stock data, interactive historical charts (up to 5 years), growth insights, and key fundamentals. Features a colorful UI with smooth animations and professional typography.

---

## 🚀 Features

* Real-time stock price lookup
* Historical charts (1 month → 5 years)
* Growth percentage (rise/fall over selected period)
* Company logo, ticker symbol, and key fundamentals
* Clean, responsive UI with animations (all CSS inline in `index.html`)

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask, yFinance, Pandas
* **Frontend:** HTML, CSS (inline in `index.html`), JavaScript
* **Visualization:** Chart.js

---

## 📂 Project Structure

```
stock-price-tracker/
│
├── app.py              # Flask backend
├── requirements.txt    # Project dependencies
└── templates/
    └── index.html      # Frontend (UI + CSS + JS)
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/stock-price-tracker.git
cd stock-price-tracker
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Flask app

```bash
python app.py
```

### 4️⃣ Open in Browser

Visit 👉 `http://127.0.0.1:5000/`

---

## 📊 Example Usage

1. Enter a stock symbol (e.g., AAPL, TSLA).
2. Select a time period (1m, 6m, 1y, 5y).
3. View the latest price, fundamentals, logo, and interactive chart.
4. Check rise/fall percentage for the selected period.

---
## 📦 Requirements

See `requirements.txt`

```
Flask
Flask-Cors
yfinance
pandas
numpy
requests
```

---
## ✨ Future Improvements

* Compare multiple stocks on the same chart
* Export stock data as reports (PDF/CSV)
* Add forecasting using ML models (ARIMA, LSTM)

---

## 📜 License

This project is open-source and available under the MIT License.

---


