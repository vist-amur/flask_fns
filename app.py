import datetime
import json
import random
import datetime

from Tools.scripts.make_ctype import method
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def index():
    # if request.method == 'POST':
    # r_p = get_contr(req=request.form['search'], key='69257345b1cc587c29cb45c9745a65c419a6cfc0')
    return render_template('main/index.html')


@app.route('/_get_contr')
def get_contr():
    # params = {'key': '69257345b1cc587c29cb45c9745a65c419a6cfc0', 'req': request.args.get('input', 0, type=str)}
    # response = requests.get(r'https://api-fns.ru/api/egr', params)
    # print(response.json())
    # return jsonify(result=response.json())
    dictionary = {'a': str(datetime.datetime.today()), 'b': 61, 'c': 82}
    json_string = json.dumps(dictionary, indent=4)

    return json_string

if __name__ == '__main__':
    app.run()
