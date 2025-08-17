from flask import Flask, render_template, request
import yfinance as yf
import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    stock_data = None

    if request.method == "POST":
        ticker = request.form["ticker"]
        stock = yf.Ticker(ticker)

        try:
            todays_data = stock.history(period="1d")
            price = round(todays_data["Close"].iloc[0], 2)
            stock_data = {
                "name": stock.info.get("shortName", "Unknown"),
                "ticker": ticker.upper(),
                "price": price,
                "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        except Exception as e:
            stock_data = {
                "name": "Error",
                "ticker": ticker.upper(),
                "price": "N/A",
                "timestamp": str(e)
            }

    return render_template("index.html", stock_data=stock_data)

if __name__ == "__main__":
    app.run(debug=True)
