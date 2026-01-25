from flask import Flask, jsonify, request
from random import random, randint

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return jsonify({"name": 42, "value": "Nothing"})


@app.route('/api', methods=['POST'])
def api():
    return jsonify({
        "name": random(),
        "value": request.content_length,
        "object": request.get_data(False, True, True)
    })


if __name__ == '__main__':
    app.run()
