from flask import Flask, request, jsonify
from json import dumps

from valid_keys import valid_keys
from hash import hash_text

app = Flask(__name__)


@app.route('/auth/', methods=['GET'])
def authorize_stream():
    print('stream received')
    hashed_key = hash_text(request.args['pwd'])

    if hashed_key in valid_keys:
        print('stream accepted')
        return jsonify(message='Successful login'), 201

    else:
        print('stream denied')
        return jsonify(message='Invalid stream key'), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
