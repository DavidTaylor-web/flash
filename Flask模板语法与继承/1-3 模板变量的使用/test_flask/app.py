from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    # 1. 简单数据类型的渲染
    age = 40
    money = 65.89
    name = '张三'
    # 2. 用户信息 dict
    user_info = {
        'username': '张三',
        'nickname': '三个',
        'address.city': '广州',
        'address.area': '天河'
    }
    # 3. 元组和列表
    tuple_city = ('北京', '上海', '广州', '深圳')
    list_city = ('北京', '上海', '广州', '深圳')

    # 4. 复杂的数据结构
    list_user = [
        {
            'username': '张三',
            'address': {
                'city': '广州'
            }
        },
        {
            'username': '李四',
            'address': {
                'city': '北京'
            }
        }
    ]
    return render_template('index.html',
                           age=age,
                           money=money,
                           name=name,
                           user_info=user_info,
                           tuple_city=tuple_city,
                           list_city=list_city,
                           list_user=list_user)
