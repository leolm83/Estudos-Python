from flask import Flask,render_template
#ponto de inicio do programa, é necessario apontar para este arquivo  no terminal: export FLASK_APP=002/hello.py

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)
