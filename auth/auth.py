from flask import Flask, request, jsonify
from json import dumps

from valid_keys import valid_keys
from hash import hash_text

app = Flask(__name__)


@app.route('/auth', methods=['GET'])
def authorize_stream():
    hashed_key = hash_text(request.args['pwd'])

    if hashed_key in valid_keys:
        return jsonify(message='Successful login'), 201

    else:
        return jsonify(message='Invalid stream key'), 401

if __name__ == '__main__':
    app.run(host='rtmp_auth', debug=True, port=5000)
