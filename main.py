import json

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    app.logger.info('V2: get call received.')
    return json.dumps({'message': 'Hello World'}), 200, {'ContentType': 'application/json'}


@app.route('/health')
def health():
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


app.run(host='0.0.0.0', port=8080)
