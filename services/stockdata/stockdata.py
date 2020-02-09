from flask import Flask
app = Flask(__name__)
cors = CORS(app)


@app.route('/')
def stock_data():
    return 'you got the stock data'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8082)