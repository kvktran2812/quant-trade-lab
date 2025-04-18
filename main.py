# server.py
from aiohttp import web
import json

async def handle_fetch_stock(request):
    data = await request.json()
    ticker = data["ticker"]
    # Simulate fetching stock data (replace with yfinance/API)
    fake_data = {"price": 150.25, "ticker": ticker}
    return web.json_response(fake_data)

app = web.Application()
app.router.add_post("/fetch_stock", handle_fetch_stock)

if __name__ == "__main__":
    web.run_app(app, port=8080)  # Access at http://localhost:8080