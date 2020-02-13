
from flask import Flask
from flask import request
from flask_cors import CORS
from calculator_funcs import calc

app = Flask(__name__)
CORS(app)


@app.route('/calc', methods=['GET', 'POST'])
def calculat():
    if request.method == 'POST':
        if request.is_json:
            return calc(request.json)
        else:
            return 'post a json object in the form\{op_a\:int, op_b\:int, oper\:int\}'
    else:
        return "oops"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8083)