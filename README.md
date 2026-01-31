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

> 注：OpenBB API 的 provider key 需配置到 OpenBB 设置里（见 OpenBB 文档）。

4) 启动 OpenBB API（如未启动）
```bash
C:\Users\ralph\IdeaProject\OpenBB\.venv\Scripts\openbb-api.exe
```

5) 运行示例
```bash
.\.venv\Scripts\python.exe scripts\crypto_demo_api.py
```

## 项目结构

```
openbb-crypto/
  scripts/            # 脚本
  data/               # 输出数据
  README.md
```
