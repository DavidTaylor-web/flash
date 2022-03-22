from flask import Flask
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def hello_world():
    """ 视图函数 """
    return 'hello_world, success'


@app.route('/user/')
@app.route('/user/<page>')
def list_user(page=1):
    return '您好，你是第{}页用户'.format(page)


app.add_url_rule('/home', 'home', hello_world)

print(app.url_map)

# v1.0之后的版本，不推荐的写法
# if __name__ == '__main__':
#    app.run()