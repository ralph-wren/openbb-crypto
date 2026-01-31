const API_BASE = "http://127.0.0.1:8000/api"; // 本地代理

let priceChart, rsiChart;

function movingAvg(data, window) {
  const out = Array(data.length).fill(null);
  for (let i = window - 1; i < data.length; i++) {
    const slice = data.slice(i - window + 1, i + 1);
    out[i] = slice.reduce((a,b)=>a+b,0) / window;
  }
  return out;
}

function rsi(values, period=14) {
  const out = Array(values.length).fill(null);
  for (let i = period; i < values.length; i++) {
    let gains = 0, losses = 0;
    for (let j = i - period + 1; j <= i; j++) {
      const diff = values[j] - values[j-1];
      if (diff >= 0) gains += diff; else losses -= diff;
    }
    const rs = losses === 0 ? 100 : gains / losses;
    out[i] = 100 - (100 / (1 + rs));
  }
  return out;
}

async function loadData() {
  const symbol = document.getElementById("symbol").value.trim();
  const interval = document.getElementById("interval").value;
  const url = `${API_BASE}/v1/crypto/price/historical?provider=yfinance&symbol=${encodeURIComponent(symbol)}&interval=${interval}`;

  const res = await fetch(url);
  if (!res.ok) {
    alert("请求失败，请确认 OpenBB API 正在运行");
    return;
  }
  const json = await res.json();
  const rows = json.results || [];
  if (!rows.length) {
    alert("无数据");
    return;
  }
  const labels = rows.map(r => r.date.slice(0,10));
  const close = rows.map(r => r.close);
  const ma20 = movingAvg(close, 20);
  const ma50 = movingAvg(close, 50);
  const rsi14 = rsi(close, 14);

  document.getElementById("lastClose").textContent = close[close.length-1].toFixed(2);
  document.getElementById("ma20").textContent = ma20[ma20.length-1] ? ma20[ma20.length-1].toFixed(2) : "-";
  document.getElementById("rsi14").textContent = rsi14[rsi14.length-1] ? rsi14[rsi14.length-1].toFixed(2) : "-";

  if (priceChart) priceChart.destroy();
  priceChart = new Chart(document.getElementById('priceChart'), {
    type: 'line',
    data: {
      labels,
      datasets: [
        { label: 'Close', data: close, borderColor: '#21d4b5', tension: 0.25 },
        { label: 'MA20', data: ma20, borderColor: '#f5b86c', tension: 0.25 },
        { label: 'MA50', data: ma50, borderColor: '#5a7fff', tension: 0.25 },
      ]
    },
    options: {
      responsive: true,
      scales: {
        x: { ticks: { color: '#93a2b7' }, grid: { color: 'rgba(255,255,255,0.05)' } },
        y: { ticks: { color: '#93a2b7' }, grid: { color: 'rgba(255,255,255,0.05)' } },
      },
      plugins: { legend: { labels: { color: '#e6edf7' } } }
    }
  });

  if (rsiChart) rsiChart.destroy();
  rsiChart = new Chart(document.getElementById('rsiChart'), {
    type: 'line',
    data: {
      labels,
      datasets: [
        { label: 'RSI14', data: rsi14, borderColor: '#f5b86c', tension: 0.25 },
      ]
    },
    options: {
      responsive: true,
      scales: {
        x: { ticks: { color: '#93a2b7' }, grid: { color: 'rgba(255,255,255,0.05)' } },
        y: { min: 0, max: 100, ticks: { color: '#93a2b7' }, grid: { color: 'rgba(255,255,255,0.05)' } },
      },
      plugins: { legend: { labels: { color: '#e6edf7' } } }
    }
  });
}

document.getElementById("load").addEventListener("click", loadData);
loadData();
