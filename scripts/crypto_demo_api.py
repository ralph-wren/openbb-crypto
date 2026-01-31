import os
import requests

BASE = "http://127.0.0.1:6900/api/v1"
FMP_API_KEY = os.getenv("FMP_API_KEY")
if not FMP_API_KEY:
    try:
        import winreg
        for root, path in [
            (winreg.HKEY_CURRENT_USER, "Environment"),
            (winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment"),
        ]:
            try:
                with winreg.OpenKey(root, path) as key:
                    FMP_API_KEY, _ = winreg.QueryValueEx(key, "FMP_API_KEY")
                    if FMP_API_KEY:
                        break
            except Exception:
                continue
    except Exception:
        FMP_API_KEY = None

# 1) 历史价格（BTC-USD，yfinance）
resp = requests.get(
    f"{BASE}/crypto/price/historical",
    params={"provider": "yfinance", "symbol": "BTC-USD"},
)
resp.raise_for_status()
print("BTC-USD 历史价格(前3条):")
print(resp.json().get("results", [])[:3])

# 2) 搜索加密资产（FMP 直连，示例：BTC）
if not FMP_API_KEY:
    print("\n提示：未检测到 FMP_API_KEY（系统环境变量）。")
else:
    fmp_resp = requests.get(
        "https://financialmodelingprep.com/api/v3/search",
        params={"query": "BTC", "limit": 10, "exchange": "crypto", "apikey": FMP_API_KEY},
        timeout=15,
    )
    if fmp_resp.status_code == 403:
        print("\n提示：FMP 返回 403（可能是 Key 无权限或额度不足）。")
    else:
        fmp_resp.raise_for_status()
        data = fmp_resp.json()
        print("\nFMP 搜索 BTC(前3条):")
        print(data[:3])
