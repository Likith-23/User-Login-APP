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
    username = request.form.get('username')
    password = request.form.get('password')
    if username == USERNAME and password == PASSWORD:
        return """
    <html>
    <head><title>WELCOME!!!</title></head>
    <body>
    <h1>:) welcome, {}</h1>
    <p>YOU HAVE SUCCESSFULLY LOGGED INN!</p>
    </body>
    </html>
    """.format(username)
    else:
        return """
    <html>
    <head><title>LOGIN FAILURE</title></head>
    <body>
    <h1>LOGIN HAS UNFORTUNATELY AND SUCCESSFULLY FAILED</h1>
    <p>Incorrect username or password, pls try again</p>
    <a href="/">back to login<a>
    </body>
    </html>
    """
if __name__ == '__main__':
    app.run(debug=True)