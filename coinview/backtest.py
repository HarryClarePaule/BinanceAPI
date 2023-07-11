import backtrader as bt
import matplotlib
import datetime

class RSIStrategy(bt.Strategy):
    
    def __init__(self):
        self.rsi = bt.talib.RSI(self.data, period=14)

    def next(self):
        if self.rsi < 30 and not self.position:
            self.buy(size=1)

        if self.rsi > 70 and self.position:
            self.close()


cerebro = bt.Cerebro()

# Increase the initial cash
# cerebro.broker.setcash(50000.0)

fromDate = datetime.datetime.strptime('2023-07-01', '%Y-%m-%d')
toDate = datetime.datetime.strptime('2023-07-10', '%Y-%m-%d')
data = bt.feeds.GenericCSVData(dataname='2023_15mins.csv', dtformat=2, compression=15, timeframe=bt.TimeFrame.Minutes, fromdate=fromDate, todate=toDate) # compression is used to specify the time frame you are trading

cerebro.adddata(data)

cerebro.addstrategy(RSIStrategy)

cerebro.run()

cerebro.plot()