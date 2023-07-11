import config
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import csv

client = Client(config.API_KEY, config.API_SECRET)

# candles = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_15MINUTE)

csvfile = open('2023_15mins.csv', 'w', newline='')
candlestick_writer = csv.writer(csvfile, delimiter=',')

# candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "1 Jan, 2023", "9 Jul, 2023")
# candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "1 Jan, 2017", "11 Jul, 2023")
# candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_15MINUTE, "1 Jan, 2020", "12 Jul, 2020")
candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_15MINUTE, "1 Jan, 2023", "10 Jul, 2023")


for candlestick in candlesticks:
    candlestick[0] = candlestick[0] / 1000
    candlestick_writer.writerow(candlestick)

csvfile.close()