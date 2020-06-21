import yfinance as yf

msft = yf.Ticker("MSFT")
msft.history(period="1y")
