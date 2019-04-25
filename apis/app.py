from flask import Flask, render_template, request, redirect
from . import myfunctions
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/api/info*": {"origins": "*"}})


# 视图部分
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/login/', methods=['GET', 'POST'])
def login1():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username, password)
        if username == 'admin' and password == 'admin':
            return redirect('/')


@app.route('/news/')
def get_news():
    pass

# api部分
@app.route('/api/', methods=['GET'])
def get_all_apis():
    """返回所有的api调用接口"""
    return myfunctions.get_all_apis()


@app.errorhandler(404)
def not_fund(error):
    return myfunctions.not_found()


@app.route('/api/info/', methods=['GET'])
def get_info():
    return myfunctions.get_info()


@app.route('/api/login/')
def login():
    return myfunctions.login()
