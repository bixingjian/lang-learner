from flask import Flask, render_template, request

app = Flask(__name__)


# 创建了 /show/info和index函数的对应关系
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/login", methods=["GET", "POST"])
def login():  # 这里get就是看这个页面(比如刷新的时候就是发送get请求) post就是提交数据
    if request.method == "GET":
        return render_template("login.html")
    else:
        user = request.form.get("username")
        pwd = request.form.get("password")
        print(user, pwd)
        return "login successful!"


@app.route("/say_the_numer", methods=["GET", "POST"])
def goto_say_the_number():
    return render_template("say_the_number.html")


@app.route("/say_the_number/get/pron", methods=["GET"])
def show_pron():
    # 接收用户通过GET形式发送的数据 [GET能够通过URL和表单提交, 一般是URL, 所以是args. POST只能通过表单提交, 所以是request.form]
    print(request.args)
    print(request.args.get("Japanese"))
    return "show pron"


@app.route("/say_the_number/post/pron", methods=["POST"])  # 这个网址只能接收POST请求
def post_pron():
    # 接收用户通过POST形式发送的数据
    print(request.form)
    print(request.form.get("ger"))
    return "show pron"





if __name__ == '__main__':
    app.run()
