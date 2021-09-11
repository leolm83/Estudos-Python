from flask import Flask,request

app = Flask(__name__)
#app.add_url_rule('/','index',index) é o mesmo que @app.route("/")
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
#rotas dinamicas
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {} !</h1>'.format(name)

@app.route('/meunavegador')
def navegador():
    user_agent=request.headers.get('User-Agent')
    return '<p>O seu browser é {}</p>'.format(user_agent)
