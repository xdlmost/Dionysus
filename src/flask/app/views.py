from app import app
from flask import request, jsonify
@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/login')
def login():
    return '<form action="/api/login" method="post" name="login"><p>name: <input type="text" name="fname"/></p><p>password: <input type="text" name="fpwd"/></p><p><input type="submit" value="Sign In"></p></form>'

@app.route('/api/login', methods=['GET', 'POST'])
def apilogin():
    if request.form["fname"]=="hehe" and request.form["fpwd"]=="hehe":
        return "KO!!"
    else:
        return  "Bad login"