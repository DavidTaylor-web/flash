from flask import Flask, render_template

app = Flask(__name__)


@app.route('/login')
def login():
    """  用户登录 """
    return render_template('login.html')


@app.route('/mine')
def course():
    """  个人中心 """
    return render_template('mine.html')

