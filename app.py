from flask import Flask

app = Flask(__name__)

# 创建了 /show/info和index函数的对应关系
@app.route("/show/info")
def index():
    return "this is good"

if __name__ == '__main__':
    app.run()