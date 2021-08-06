# https://github.com/newnewcoder/flask-hls-demo/blob/master

from flask import Flask, request, jsonify, render_template
from json import dumps
from sys import stderr
from hash import hash_text

app = Flask(__name__)

streams = {}

# add your stream key and hashed password here
keys = {
    'stream_key': 'hashed stream password (paste here from hash.py)',
}


@app.route('/auth', methods=['GET'])
def authorize_stream():
    stream_key = str(request.args['name'])

    # prevents a KeyError when searching the dictionary later
    if stream_key not in streams:
        streams[stream_key] = False

    if keys[stream_key] == hash_text(request.args['pwd']):
        # check if there's already a stream active under stream key. If false (stream inactive), allow and set to true
        if not streams[stream_key]:
            print(f'Stream Key accepted: {stream_key}', file=stderr)
            streams[stream_key] = True
            return jsonify(message='Successful login'), 201

        else:
            print(f'Stream already active: {stream_key}', file=stderr)
            return jsonify(message='Stream already active'), 405

    else:
        return jsonify(message='Invalid stream key'), 401


@app.route('/stream_done', methods=['GET'])
def stream_done():
    stream_key = str(request.args['name'])
    streams[stream_key] = False
    print(f'Stream completed: {stream_key}', file=stderr)
    return jsonify(message='Stream ended successfully'), 200


# allow webserver container to get a list of active streams
@app.route('/active_streams', methods=['GET'])
def get_active():
    return jsonify(streams), 200


if __name__ == '__main__':
    app.run(host='auth_server', debug=True, port=5000)
