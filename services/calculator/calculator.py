
from flask import Flask
from flask import request
from calculator_funcs import calc

app = Flask(__name__)
cors = CORS(app)


@app.route('/calc', methods=['GET', 'POST'])
def calculat():
    if request.method == 'POST':
        return calc(request.json())
    else:
        return "oops"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8083)