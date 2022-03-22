from flask import Flask, render_template, render_template_string, g, url_for

app = Flask(__name__)


@app.route('/')
def index():

    # return render_template('index.html')
    html = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h1>欢迎你</h1>
</body>
</html>
    """
    return render_template_string(html)


@app.before_request
def before_request():
    g.user = 'zhangsan'


@app.context_processor
def inject_user():
    return dict(user=g.user)


@app.route('/html')
def html():
    return render_template('index.html')


@app.route('/mine2')
def mine():
    """ 我的 """
    print(url_for('html', _external=True))
    print(url_for('mine', _external=True))
    return render_template('mine.html')