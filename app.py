from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "这次可以了吗"
