import pandas as pd
import requests

BNB_DESCRIPTION = """
Binance coin (BNB) is the exchange token of the Binance crypto exchange. It was launched originally on the Ethereum blockchain but later migrated to the Binance Smart Chain, now called BNB Chain.

Holders of BNB with Binance accounts can access discounted fees on the exchange. That means demand for the token is linked to demand for the exchange’s services. Therefore, buying BNB can be seen as a bet on the success of the exchange, in a similar way to buying a share in a company, except that owning the token comes with no ownership rights in the exchange.
"""

def get_historic_price(symbol, exchange="binance", after="2018-09-01"):
    url = "https://api.cryptowat.ch/markets/{exchange}/{symbol}usdt/ohlc".format(
        symbol=symbol, exchange=exchange)
    resp = requests.get(url, params={
        "periods" : "3600",
        "after" : str(int(pd.Timestamp(after).timestamp()))
    })
    resp.raise_for_status()
    data = resp.json()
    df = pd.DataFrame(data["result"]["3600"], columns=[
                'CloseTime', 'OpenPrice', 'HighPrice', 'LowPrice', 'ClosePrice', 'Volume', 'NA'
    ])
    df['CloseTime'] = pd.to_datetime(df['CloseTime'], unit='s')
    df.set_index('CloseTime', inplace=True)
    return df

