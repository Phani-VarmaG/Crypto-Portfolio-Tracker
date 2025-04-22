import requests

def get_coin_prices(coin_ids):
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'usd',
        'ids': ','.join(coin_ids),
        'price_change_percentage': '1h,24h,7d'
    }
    response = requests.get(url, params=params)
    return {item['id']: item for item in response.json()}

async def update_prices_continuously():
    while True:
        coins = get_all_coins_from_db()
        prices = get_coin_prices(coins)
        update_portfolio_values(prices)
        await asyncio.sleep(300)  # Update every 5 minutes
