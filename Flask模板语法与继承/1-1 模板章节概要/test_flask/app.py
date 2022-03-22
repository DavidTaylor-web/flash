import os
from datetime import datetime

from flask import Flask,render_template
app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@app.route('/html')
def html_from_file():
    """ 把html文件的内容在浏览器展现出来"""
    return render_template('index.html')


@app.route('/show/html')
def html_show():
    """ 理解渲染机制 """
    # 1. 找到磁盘上的html文件地址（全路径）
    file_name = os.path.join(os.path.dirname(__file__), 'templates', 'index.html')
    print(file_name)
    # 2. 读取html文件中的内容
    now_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(file_name, 'r', encoding='utf-8') as f:
        html = f.read()
        # 3. 替换html中的特殊字符（{{time}}）
        html = html.replace('{{time}}', now_time)
        # 4. 将html的内容发送给浏览器
        return html



