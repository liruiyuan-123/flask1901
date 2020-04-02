# python自带的
import os
import sys

# 第三方库
import click
from flask import Flask,render_template
# 导入扩展类
from flask_sqlalchemy import SQLAlchemy 

WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

app = Flask(__name__)
# linux下四条杠
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////'+os.path.join(app.root_path,'data.db')
# Windows下三条杠
app.config['SQLALCHEMY_DATABASE_URI'] = prefix+os.path.join(app.root_path,'data.db')
# 关闭了对模型修改的监控
app.config['SQLALCHY_TRACK_MODIFICATIONS'] = False
# 初始化扩展，传入程序实例app
db = SQLAlchemy(app)

# models
class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))

class Movie(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(60))
    year = db.Column(db.String(4))

# views
@app.route('/')
def index():
    name = "Bruce"
    movies = [
        {"title":"我是谁","year":"2016"},
        {"title":"我是谁","year":"2016"},
        {"title":"我是谁","year":"2016"},
        {"title":"我的父亲母亲","year":"1995"},
        {"title":"囧妈","year":"2020"},
        {"title":"战狼","year":"2020"},
        {"title":"心花路放","year":"2018"},
        {"title":"囧妈","year":"2020"},
        {"title":"战狼","year":"2020"},
    ]
    return render_template('index.html',name=name,movies=movies)
    

# 自定义命令
@app.cli.command()  #装饰器，注册命令
@click.option('--drop',is_flag=True,help="删除后再创建")
def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo("初始化数据库完成")



# 动态URL
# @app.route('/index/<name>')
# def home(name):
#     print(url_for('home',name="Bruce"))
#     return "<h1>Hello，%s</h1>"%name