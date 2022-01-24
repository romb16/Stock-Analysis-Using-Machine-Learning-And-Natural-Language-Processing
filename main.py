import finnhub
import pandas as pd
from Scripts.config import token
import json
from datetime import datetime
from dateutil.relativedelta import relativedelta
from collections import defaultdict


if __name__ == '__main__':

    # Initialize client interface to finnhub API
    finnhub_client = finnhub.Client(api_key=token)

    # Obtain current date
    today = datetime.now()

    # Calculate date 10 days ago from current date and format date
    tendaysago = (today - relativedelta(days=10)).date().strftime("%Y-%m-%d")
    print(tendaysago)

    # Change today date format
    today = today.strftime("%Y-%m-%d")
    # print(today)

    # Obtain company stock candles for given linux date time frame and stock
    # res = finnhub_client.stock_candles('NVDA', 'D', 1590988249, 1591852249)
    # print(res)
    # print()

    # Frame data and print
    # print(pd.DataFrame(res))
    # print()

    # Obtain company stock news from 10 days ago to todays date of a stock
    newsdata = finnhub_client.company_news('NVDA', _from=tendaysago, to=today)
    # print(newsdata)

    # Dictionary containing date time and list of URLs for Yahoo news articles
    yahoo_URLs = defaultdict(list)

    for news in newsdata:

        # Format news data date time to format yyyy-mm-dd
        news['datetime'] = datetime.fromtimestamp(news['datetime']).strftime("%Y-%m-%d")

        # View news from Yahoo only
        if news['source'] == 'Yahoo':

            # Set key to date time and append URL to list
            yahoo_URLs[news['datetime']].append(news['url'])
            #print(news)
            #print()

    for date, URLS in yahoo_URLs.items():

        print(date)
        print(URLS)
        print()
