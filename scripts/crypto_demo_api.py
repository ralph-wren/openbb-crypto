import requests

BASE = "http://127.0.0.1:6900/api/v1"

# 1) 历史价格（BTC-USD，yfinance）
resp = requests.get(
    f"{BASE}/crypto/price/historical",
    params={"provider": "yfinance", "symbol": "BTC-USD"},
)
resp.raise_for_status()
print("BTC-USD 历史价格(前3条):")
print(resp.json().get("results", [])[:3])

# 2) 搜索加密资产（示例：BTC）
resp = requests.get(
    f"{BASE}/crypto/search",
    params={"provider": "fmp", "query": "BTC"},
)
if resp.status_code == 400 and "fmp_api_key" in resp.text:
    print("\n提示：crypto/search 需要 FMP API Key。请先配置 fmp_api_key 后再试。")
else:
    resp.raise_for_status()
    print("\nCrypto 搜索 BTC(前3条):")
    print(resp.json().get("results", [])[:3])
