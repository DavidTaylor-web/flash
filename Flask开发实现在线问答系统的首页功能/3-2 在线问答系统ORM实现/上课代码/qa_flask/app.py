from datetime import datetime

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

import constants

app = Flask(__name__, static_folder='assets')
# 数据库的配置URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flask_qa'

db = SQLAlchemy(app)


class User(db.Model):
    """ 用户模型 """
    __tablename__ = 'accounts_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 用户名，用于登录
    username = db.Column(db.String(64), unique=True, nullable=False)
    # 用户昵称
    nickname = db.Column(db.String(64))
    password = db.Column(db.String(256), nullable=False)
    # 用户的头像地址
    avatar = db.Column(db.String(256))
    # 用户是否可以登录系统
    status = db.Column(db.SmallInteger,
                       default=constants.UserStatus.USER_ACTIVE.value,
                       comment='用户状态')
    # 是否是超级管理员，管理员可以对所有的内容进行管理
    is_super = db.Column(db.SmallInteger, default=constants.UserRole.COMMON.value)
    # 注册时间
    created_at = db.Column(db.DateTime, default=datetime.now)
    # 更新时间
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    # profile = db.relationship('UserProfile')


class UserProfile(db.Model):
    """ 用户的详细信息 """
    __tablename__ = 'accounts_user_profile'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 冗余字段
    username = db.Column(db.String(64), unique=True, nullable=False)
    # 关联用户
    user_id = db.Column(db.Integer, db.ForeignKey('accounts_user.id'))
    # 建立用户的一对一关系属性user.profile  profile.user
    user = db.relationship('User', backref=db.backref('profile', uselist=False))


@app.route('/')
def index():
    """ 首页 """
    return render_template('index.html')


@app.route('/follow')
def follow():
    """ 关注 """
    return render_template('follow.html')


@app.route('/login')
def login():
    """ 登录页面 """
    return render_template('login.html')


@app.route('/register')
def register():
    """ 注册 """
    return render_template('register.html')


@app.route('/write')
def write():
    """ 写文章，提问 """
    return render_template('write.html')


@app.route('/mine')
def mine():
    """ 个人中心 """
    return render_template('mine.html')


@app.route('/detail')
def detail():
    """ 问题详情 """
    return render_template('detail.html')
