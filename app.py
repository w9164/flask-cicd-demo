from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "可恶啊 还是不行嘛"
