from flask import Flask, render_template
app = Flask(__name__)
port = 5000


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/pedigrees')
def pedigrees():
    return render_template("pedigree.html")


app.run(port=port, debug=True)
