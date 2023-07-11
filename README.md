# BinanceAPI

## Step 1 - Websockets & Lghtweight Charts
* Create realtime light-weight charts in javascript
* wscat - connect to websocket from the command line
* Capture output to text file
* UI to check technical indicators (RSI, SMA), configure alerts & notifications

## Step 2 - Technical analysis with python and TAlib
* Connect to webockets with python
* Write candlestick data to csv
* Install TALIB, anlysis technical indicators on a dataset

## Step 3 - Backtesting with backtrader and TAlib Indicators
* Test indicators against historical dataset
* Plot pretty charts with buy and sell points


### Addiitonal notes
* The base endpoint is: wss://stream.binance.com:9443 or wss://stream.binance.com:443
* wss://stream.binance.com:9443/ws/btcusdt@trade
* < {"e":"trade","E":1688496453388,"s":"BTCUSDT","t":3163009968,"p":"30906.90000000","q":"0.00157000","b":21682983268,"a":21682984519,"T":1688496453388,"m":true,"M":true}
* wscat -c wss://stream.binance.com:9443/ws/btcusdt@kline_1m
* < {"e":"kline","E":1688496597174,"s":"BTCUSDT","k":{"t":1688496540000,"T":1688496599999,"s":"BTCUSDT","i":"1m","f":3163010513,"L":3163010912,"o":"30913.15000000","c":"30913.14000000","h":"30915.90000000","l":"30913.14000000","v":"11.15109000","n":400,"x":false,"q":"344725.95135980","V":"2.72830000","Q":"84341.81305240","B":"0"}}
* unix time stamp can be used to convert the time stamp
* wscat -c wss://stream.binance.com:9443/ws/btcusdt@kline_1m > dataset.txt