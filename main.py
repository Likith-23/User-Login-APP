from flask import Flask, request, redirect, url_for
app = Flask(__name__)
USERNAME = 'Likith'
PASSWORD = 'PASSWORD123'
@app.route('/', methods=['GET'])
def login_form():
    return """
<html>
<head>
<title>Login</title>
</head>
<body>
<h2>LOGIN</h2>
<form action="/login" method="post">
<label for = "username">username</label>
<input type="text" id="username" name="username"><br><br>
<label for = "password">password</label>
<input type="password" id="password" name="password"><br><br>
<input type="submit" value="login">
</form>
</body>
</html>
"""
@app.route('/login', methods=['POST'])
def login():
    USERNAME = request.form.get('username')
    PASSWORD = request.form.get('password')