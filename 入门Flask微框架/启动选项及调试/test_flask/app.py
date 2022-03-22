from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def hello_world():
    return 'hello_world, success'

# v1.0之后的版本，不推荐的写法
# if __name__ == '__main__':
#    app.run()