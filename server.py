from flask import Flask, render_template
app = Flask(__name__)
port = 5000


@app.route('/')
def hello_world():
    return render_template("index.html")


app.run(port=port, debug=True)
