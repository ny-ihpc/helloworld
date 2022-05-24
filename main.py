import logging

from flask import Flask

app = Flask(__name__)
app.logger.setLevel(logging.INFO)


@app.route('/')
def index():
    app.logger.info('V2: get call received.')
    data = {'message': 'Hello World'}
    return data, 200


@app.route('/health')
def health():
    data = {'success': True}
    return data, 200


app.run(host='0.0.0.0', port=8080)
