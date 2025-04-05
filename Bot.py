import requests
import pandas as pd
import time

def fetch_stock_data(symbol):
    return {
        "price": 100,
        "rsi": 55,
        "macd": 0.5,
        "bollinger": (95, 105)
    }

def generate_signal(data):
    if data["rsi"] < 30 and data["price"] < data["bollinger"][0]:
        return "BUY"
    elif data["rsi"] > 70 and data["price"] > data["bollinger"][1]:
        return "SELL"
    return "HOLD"

def main():
    symbol = "RELIANCE"
    while True:
        stock_data = fetch_stock_data(symbol)
        signal = generate_signal(stock_data)
        print(f"{symbol}: {signal} at {stock_data['price']}")
        time.sleep(60)

if __name__ == "__main__":
    main()
