from flask import Flask, render_template

# from flask import jsonify

app = Flask(__name__)


@app.route("/")
@app.route("/hello")
def Helloworld():
    return "heloo me"

if __name__ == '__main__':
    debug = True
    app.run()