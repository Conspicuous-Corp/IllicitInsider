from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def scrape_stock_data():
    return 'Hello, World TEST@@@'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8081)