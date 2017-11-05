# pylint: disable=C0103, C0111, R0914

'''
Main server file
'''

from flask import Flask, request, jsonify
from inshorts import getNews

app = Flask(__name__)

@app.route('/news', methods=['GET', 'POST'])

def news():
    if request.method == 'POST':
        return jsonify(getNews(request.form['category']))
    elif request.method == 'GET':
        return jsonify(getNews(request.args.get('category')))

app.run(debug=True)
        