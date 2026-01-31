import requests
import pandas as pd

BASE = "http://127.0.0.1:6900/api/v1"

# 拉取历史价格（BTC-USD）
resp = requests.get(
    f"{BASE}/crypto/price/historical",
    params={"provider": "yfinance", "symbol": "BTC-USD", "interval": "1d"},
)
resp.raise_for_status()
rows = resp.json().get("results", [])

if not rows:
    raise SystemExit("no data")

# 构建 DataFrame
_df = pd.DataFrame(rows)
_df["date"] = pd.to_datetime(_df["date"])
_df = _df.sort_values("date")

# 计算指标
_df["ma20"] = _df["close"].rolling(20).mean()
_df["ma50"] = _df["close"].rolling(50).mean()

# RSI(14)
chg = _df["close"].diff()
gain = chg.clip(lower=0)
loss = -chg.clip(upper=0)
roll_up = gain.rolling(14).mean()
roll_down = loss.rolling(14).mean()
rs = roll_up / roll_down
_df["rsi14"] = 100 - (100 / (1 + rs))

print(_df.tail(5)[["date", "close", "ma20", "ma50", "rsi14"]])
