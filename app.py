from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "我喜欢你啊"
