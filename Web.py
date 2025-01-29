from flask import Flask,render_template

app = Flask(__name__)

@app.route("/show/info")
def show_info():
    return render_template("index.html")

@app.route("/get/news")
def get_news():
    return render_template("news.html")

if __name__ == '__main__':
    app.run(port="8000")