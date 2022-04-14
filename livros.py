from flask import Flask, render_template

app = Flask(__name__)


@app.route('/index')
def ola():
    return render_template('lista.html', titulo='minhaBiblioteca')


app.run()
