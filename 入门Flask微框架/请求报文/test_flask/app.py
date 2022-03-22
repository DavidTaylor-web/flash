from flask import Flask, current_app, g, request, session
app = Flask(__name__)


@app.route('/index')
def index():
    print(app)
    print(current_app)
    print(app == current_app)
    print(app is current_app)
    return 'index'


@app.route('/')
def hello_world():
    """ 视图函数 """
    return 'hello_world, success'


@app.route('/user/')
@app.route('/user/<page>')
def list_user(page=1):
    return '您好，你是第{}页用户'.format(page)


@app.route('/test/req')
def test_request():
    """ 请求报文练习 """
    get_args = request.args
    print(get_args)
    # 页码一定是正整数
    page = request.args.get('page', 1)
    print(page)
    # 服务器所在的主机地址
    headers = request.headers
    print(headers)
    print(headers.get('host'))
    # 获取ip地址
    ip = request.remote_addr
    print('远程IP地址')
    print(ip)

    # 获取User-agent
    user_agent = request.headers.get('user-agent', None)
    print('User-Agent：')
    print(user_agent)

    return 'request success'


@app.before_first_request
def first_request():
    """ 服务器启动后第一个请求到达 """
    print('first_request')


@app.before_request
def per_request():
    """ 每一个请求到达前 """
    print('before request')
