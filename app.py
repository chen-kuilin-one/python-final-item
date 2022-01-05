from flask import Flask, request
from flask import render_template
# 此代码用于调用自定义模块中的函数
from reserch import reserch4letters

app = Flask(__name__)


# 【Flask】(https://dormousehole.readthedocs.io/en/latest/quickstart.html#id10)
# 【HTMl】(https://www.w3school.com.cn/html/index.asp)
# 【jinja2】(https://palletsprojects.com/p/jinja/)

# 1. 路由：相对路径，决定了 页面资源 的路径，如果没有登记，将返回404 not found
# 1.1 url: 相对于：http://127.0.0.1：5000的相对路径
# 1.2 methods:【GET】【POST】
# 2. 视图函数：
# 2.1 函数过程决定了你操作的方法（实现的功能），例如 if elif else for while ...
# 2.2 return：返回数据内容，text文本，HTML文件（模板渲染），JSON文件等

# 【GET】
@app.route('/', methods=['GET'])
def welcome():
    return render_template('welcome.html')


@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/index_1', methods=['GET'])
def index_1():
    return render_template('index_1.html')


@app.route('/index_2', methods=['GET'])
def index_2():
    return render_template('index_2.html')


# 【POST】实现用户输入，点击提交，将数据提交到 /result
@app.route('/result', methods=['POST'])
def result():
    print(request)
    py_firstname = request.form['firstname']
    print(py_firstname)
    py_lastname = request.form['lastname']
    py_fullname = py_firstname.title() + ' ' + py_lastname.title()

    return render_template('result.html',
                           fullname=py_fullname,
                           )


@app.route('/result_1', methods=['POST'])
def result_1():
    py_word = request.form['word']
    py_vowels = request.form['vowels']
    py_found = reserch4letters(py_vowels, py_word)

    return render_template('result.html',
                           found=py_found,
                           )


@app.route('/result_2', methods=['POST'])
def result_2():
    py_number = request.form['number']
    py_money = 2350 - int('3') * 68

    return render_template('result.html',
                           money=py_money,
                           )


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route('/shopping_center', methods=['GET', 'POST'])
def shopping_center():
    return render_template('shopping_center.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
