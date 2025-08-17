import yfinance as yf
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

def fetch_and_plot():
    symbol = symbol_entry.get().upper()
    period = period_var.get()

    if not symbol:
        messagebox.showerror("Input Error", "Please enter a stock symbol.")
        return

    try:
        data = yf.download(symbol, period=period)

        if data.empty:
            messagebox.showinfo("No Data", "No data found for the given symbol and period.")
            return

        plt.figure(figsize=(10, 5))
        plt.plot(data.index, data['Close'], label='Close Price', color='blue')
        plt.title(f"{symbol} Stock Price - {period}")
        plt.xlabel("Date")
        plt.ylabel("Price (USD)")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch data.\n{str(e)}")

# GUI setup
root = tk.Tk()
root.title("Stock Price Tracker")
root.geometry("400x250")
root.resizable(False, False)

# Input widgets
tk.Label(root, text="Enter Stock Symbol (e.g. AAPL):").pack(pady=10)
symbol_entry = tk.Entry(root, width=30)
symbol_entry.pack()

tk.Label(root, text="Select Period:").pack(pady=5)
period_var = tk.StringVar(value="1mo")
period_options = ["5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "max"]
tk.OptionMenu(root, period_var, *period_options).pack()

tk.Button(root, text="Track Stock", command=fetch_and_plot, bg="blue", fg="white").pack(pady=20)

root.mainloop()
