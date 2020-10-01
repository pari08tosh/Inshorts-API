# pylint: disable=C0103, C0111, R0914

'''
Main server file returning the news dictionary from inshorts file as JSON Object
'''

from flask import Flask, request, jsonify
from inshorts import getNews
from flask_cors import CORS
env= 1
# If deploying on cloud server such as heroku use env =0  else use development server ie env = 1
app = Flask(__name__)
CORS(app)

@app.route('/news', methods=['GET', 'POST'])

def news():
    if request.method == 'POST':
        return jsonify(getNews(request.form['category']))
    elif request.method == 'GET':
        return jsonify(getNews(request.args.get('category')))

    
if (env == 0):
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
else:
    app.run(debug=True)
        
