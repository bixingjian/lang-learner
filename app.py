from flask import Flask, render_template, request

app = Flask(__name__)


# 创建了 /show/info和index函数的对应关系
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/get/pron", methods=["GET"])
def show_pron():
    # 接收用户通过GET形式发送的数据 [GET能够通过URL和表单提交, 一般是URL, 所以是args. POST只能通过表单提交, 所以是request.form]
    print(request.args)
    print(request.args.get("Japanese"))
    return "show pron"


@app.route("/post/pron", methods=["POST"])  # 这个网址只能接收POST请求
def post_pron():
    # 接收用户通过POST形式发送的数据
    print(request.form)
    print(request.form.get("ger"))
    return "show pron"


@app.route("/get_pron")
def get_pron():
    return render_template("get_pron.html")


if __name__ == '__main__':
    app.run()
