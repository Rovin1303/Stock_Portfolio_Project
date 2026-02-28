import yfinance as yf

def get_stock_analysis(ticker):

    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="1y", interval="1d", auto_adjust=True)

        if hist.empty:
            return None

        info = stock.fast_info

        current_price = hist["Close"].iloc[-1]
        high_52w = hist["Close"].max()
        low_52w = hist["Close"].min()
        percent_from_high = ((current_price - high_52w) / high_52w) * 100

        percent_from_low = ((current_price - low_52w) / low_52w) * 100

        return {
            "ticker": ticker,
            "current_price": round(current_price, 2),
            "high_52w": round(high_52w, 2),
            "low_52w": round(low_52w, 2),
            "percent_from_low": round(percent_from_low, 2),
            "percent_from_high": round(percent_from_high, 2),
            "pe_ratio": info.get("trailingPE"),
            "market_cap": info.get("marketCap"),
            "sector": None,
            "industry": None,
            "price_history": hist["Close"].tolist(),
            "dates": hist.index.strftime("%Y-%m-%d").tolist()
        }

    except Exception as e:
        print("YFinance Error:", e)
        return None