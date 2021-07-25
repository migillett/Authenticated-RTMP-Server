from flask import Flask, request, jsonify
from json import dumps

from valid_keys import valid_keys
from hash import hash_text

app = Flask(__name__)


<<<<<<< Updated upstream
@app.route('/auth', methods=['GET'])
def authorize_stream():
    hashed_key = hash_text(request.args['pwd'])

    if hashed_key in valid_keys:
        return jsonify(message='Successful login'), 201

    else:
        return jsonify(message='Invalid stream key'), 401

if __name__ == '__main__':
    app.run(host='localhost', debug=True, port=5000)
=======
@app.route('/auth')
def auth():
    try:
        hashed_key = hash_text(request.args.get('pwd'))

        if hashed_key in valid_keys:
            return jsonify(message='Successful login'), 200

        else:
            return jsonify(message='Invalid stream key'), 403

    except AttributeError:
        return jsonify(message='Invalid URL'), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
>>>>>>> Stashed changes
