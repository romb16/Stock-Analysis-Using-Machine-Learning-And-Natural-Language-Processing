import finnhub
import pandas as pd
from Scripts.config import token
import json
from datetime import datetime


if __name__ == '__main__':
    finnhub_client = finnhub.Client(api_key=token)
    res = finnhub_client.stock_candles('NVDA', 'D', 1590988249, 1591852249)
    print(res)
    print(pd.DataFrame(res))
    newsdata = finnhub_client.company_news('NVDA', _from="2021-11-01", to="2022-01-01")
    for news in newsdata:
        if news['source'] == 'MarketWatch':
            dt = datetime.fromtimestamp(news['datetime']).strftime("%m/%d/%Y, %H:%M:%S")

            news['datetime'] = dt
            print(news)
            print()