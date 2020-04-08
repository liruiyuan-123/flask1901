# python自带的
import os
import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager

app = Flask(__name__)
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'


# linux下四条杠
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////'+os.path.join(app.root_path,'data.db')
# Windows下三条杠
app.config['SQLALCHEMY_DATABASE_URI'] = prefix+os.path.join(os.path.dirname(app.root_path),'data.db')
# 关闭了对模型修改的监控
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'watchlist_dev'
# 初始化扩展，传入程序实例app
db = SQLAlchemy(app)

login_manager = LoginManager(app) #实例化登录拓展类
@login_manager.user_loader
def load_user(user_id):
    from watchlistapp.models import User
    user = User.query.get(int(user_id))
    return user

login_manager.login_view = 'login'

# 模板上下文处理函数
# 返回的变量会统一注入到每一个模板的上下文
@app.context_processor
def common_user():
    from watchlistapp.models import User
    user = User.query.first()
    return dict(name=user)

from watchlistapp import views,errors,commands