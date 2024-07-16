from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

@app.route("/")
#def hello_world():
    #return "<p>Hello, World!</p>"     commande de base


def hello(name=None):
    return render_template('index.html', name=name)


if __name__=="__main__":

    app.run(debug=True)
    