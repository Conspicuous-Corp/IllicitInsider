from flask import Flask
app = Flask(__name__)

@app.route('/')
def scrape_stock_data():
    return 'Hello, World!'