import config
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
from binance.enums import *
from flask import Flask, render_template, request, flash, redirect, jsonify

client = Client(config.API_KEY_CB, config.API_SECRET_CB)

app = Flask(__name__)
app.secret_key = config.APP_SECRET_KEY

@app.route("/")
def index():
    Title = "Harry's Coinview"
    
    info = client.get_account()
    balances = info['balances']

    exchange_info = client.get_exchange_info()
    symbols = exchange_info['symbols']
    
    #print(exchange_info)
    
    # look through assets and append to list assets which have a value above 0
    active_asset = []
    for asset in balances:
        num = float(asset['free'])
        if num > 0:
            print(asset)
            active_asset.append(asset)
        

    
    return render_template('index.html', title=Title, my_balances=balances, active_Asset=active_asset, Symbols=symbols)

@app.route("/buy", methods=['POST'])
def buy():
    print(request.form)
    # quantity = request.form['quantity']
    # if not quantity:
    #     flash("Please input quantity required")
    # else:
    try:
        order = client.create_order(
        symbol=request.form['symbol'],
        side=SIDE_BUY,
        type=ORDER_TYPE_MARKET,
        quantity=request.form['quantity'],
        )
        print("Trade success")
    except Exception as e:
        flash(e.message, 'Error creating test order')

    return redirect('/')

@app.route("/sell")
def sell():
    return 'sell'

@app.route("/settings")
def settings():
    return 'settings'

@app.route("/history")
def history():
    candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_15MINUTE, "1 Jul, 2023", "9 Jul, 2023")
    processed_candlesticks = []

    for data in candlesticks:
        candlestick = { 
            "time": data[0] / 1000, #unix timesatnd in milliseconds so need to convert
            "open": data[1], 
            "high": data[2], 
            "low": data[3], 
            "close": data[4] 
            }
        processed_candlesticks.append(candlestick)


    return jsonify(processed_candlesticks)

if __name__ == '__main__':
    app.run(debug=True)