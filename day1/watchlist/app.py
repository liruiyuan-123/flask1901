from flask import Flask,render_template
app = Flask(__name__)

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
    



# 动态URL
# @app.route('/index/<name>')
# def home(name):
#     print(url_for('home',name="Bruce"))
#     return "<h1>Hello，%s</h1>"%name