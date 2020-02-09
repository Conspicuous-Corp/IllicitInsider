from flask import Flask
app = Flask(__name__)

@app.route('/')
def stock_data():
    return 'you got the stock data'
