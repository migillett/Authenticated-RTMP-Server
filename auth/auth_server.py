# https://github.com/newnewcoder/flask-hls-demo/blob/master

from flask import Flask, request, jsonify, render_template
from os import path
from json import dump, load
from sys import stderr
from hash import hash_text

app = Flask(__name__)

json_folder = path.join(path.curdir, 'stream_keys')


def load_json(stream_name):
    with open(path.join(json_folder, f'{stream_name}.json'), 'r') as json_file:
        return load(json_file)


def update_json(dict, stream_live=False):
    dict['live'] = stream_live
    with open(path.join(json_folder, f'{dict["stream_name"]}.json'), 'w') as json_file:
        dump(dict, json_file)



@app.route('/auth', methods=['GET'])
def authorize_stream():
    stream_name = str(request.args['name'])

    try:
        stream_stats = load_json(stream_name)

        if stream_stats['stream_key'] == hash_text(request.args['pwd']):
            if not stream_stats['live']:
                print(f'Stream Key accepted: {stream_stats["stream_name"]}', file=stderr)
                update_json(dict=stream_stats, stream_live=True)
                return jsonify(message='Successful login'), 201

            else:
                print(f'Stream already active: {stream_stats["stream_name"]}', file=stderr)
                return jsonify(message='ERROR: Stream already active'), 405
        else:
            print(f'ERROR: incorrect stream key', file=stderr)
            return jsonify(message='ERROR: Stream key incorrect'), 405

    except FileNotFoundError:
        return jsonify(message=f'ERROR: Stream configuration not found.'), 401


@app.route('/stream_done', methods=['GET'])
def stream_done():
    stream_stats = load_json(str(request.args['name']))
    update_json(dict=stream_stats, stream_live=False)
    print(f'Stream completed: {stream_stats["stream_name"]}', file=stderr)
    return jsonify(message='Stream ended successfully'), 200


if __name__ == '__main__':
    app.run(host='auth_server', debug=True, port=5000)
