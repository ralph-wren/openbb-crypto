# OpenBB Crypto Lab

专门用于基于 OpenBB 的加密货币数据开发与实验。

## Quick Start

1) 创建虚拟环境
```bash
py -3.12 -m venv .venv
```

2) 安装依赖
```bash
.\.venv\Scripts\python.exe -m pip install -U pip
.\.venv\Scripts\python.exe -m pip install openbb requests
```

3) 配置 API Key（系统环境变量）
```powershell
[Environment]::SetEnvironmentVariable("FMP_API_KEY","<你的key>","User")
```

4) 启动 OpenBB API（如未启动）
```bash
C:\Users\ralph\IdeaProject\OpenBB\.venv\Scripts\openbb-api.exe
```

5) 运行示例
```bash
.\.venv\Scripts\python.exe scripts\crypto_demo_api.py
```

6) 运行指标示例（MA/RSI）
```bash
.\.venv\Scripts\python.exe scripts\crypto_indicators.py
```

7) 启动可视化 Demo
```bash
.\.venv\Scripts\python.exe scripts\web_server.py
```
浏览器打开：`http://127.0.0.1:8000`

> 说明：脚本中 **历史价格** 使用 OpenBB API（yfinance），**搜索** 使用 FMP 直连（读取 FMP_API_KEY）。如遇 403，通常是 Key 权限/额度问题。

## 项目结构

```
openbb-crypto/
  scripts/            # 脚本
  data/               # 输出数据
  README.md
```
