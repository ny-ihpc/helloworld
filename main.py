from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    print('V2: get call received.')
    return 'Hello World!!!!!'

app.run(host='0.0.0.0', port=8080)
