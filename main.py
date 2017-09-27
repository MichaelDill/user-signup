import os
import html
import cgi
import jinja2
from flask import Flask, request, redirect
import string
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():

    error = request.args.get("error")
    usernameError = request.args.get("unE")
    if not usernameError:
        usernameError = ""
    
    passwordError = request.args.get("pwE")
    if not passwordError:
        passwordError = ""

    confPassWordError = request.args.get("cPwE")
    if not confPassWordError:
        confPassWordError = ""
    emailError = request.args.get("emE")
    if not emailError:
        emailError = ""


    if error:

        body = jinja_env.get_template('index.html')
        return body.render(usernameError=usernameError,passwordError=passwordError,confPassWordError=confPassWordError,emailError=emailError)

    else:

        body = jinja_env.get_template('index.html')
        return body.render(usernameError="",passwordError="",confPassWordError="",emailError="")


@app.route("/login", methods=['POST'])
def login():



    username = request.form['username']
    email = request.form['inputEmail']
    password = request.form['inputPassword']
    confPassword = request.form['confPassword']

    error = False
    errorMsg ="true"

    if username == "":
        error = True
        errorMsg += "&unE=Please enter a username"
    elif len(username) < 3 or len(username) > 20:
        error = True
        errorMsg += "&unE=Pleae enter a valid username"
    elif " " in username:
        error = True
        errorMsg += "&unE=Pleae enter a valid username"

    if password == "":
        error = True
        errorMsg += "&pwE=Please enter a password"
    elif len(password) < 3 or len(password) > 20:
        error = True
        errorMsg += "&pwE=Pleae enter a valid password"
    elif " " in password:
        error = True
        errorMsg += "&pwE=Pleae enter a valid password"
    else:
        if confPassword != password:
            error = True
            errorMsg += "&cPwE=Please confirm your password"

    if email != "":
        if "@" not in email or "." not in email or len(email) < 3 or len(email) > 20:
            error = True
            errorMsg += "&emE=Please enter a valid email"


    if error == True:
        return redirect("/?error=" + errorMsg)
    else:
        body = jinja_env.get_template('login.html')
        return body.render()

app.run()