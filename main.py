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

    if error:
        error_esc = (cgi.escape(error, quote=True)).split(",")

        error_element = '<ul>'

        for msg in error_esc:
            error_element += '<li>' + msg + '</li>'

        error_element += '</ul>'
    else:
        error_element = ''

    body = jinja_env.get_template('index.html')
    return body.render(error = error_element)


@app.route("/login", methods=['POST'])
def login():



    username = request.form['username']
    email = request.form['inputEmail']
    password = request.form['inputPassword']
    confPassword = request.form['confPassword']

    error = False
    errorMsg ="Error Details:"

    if username == "":
        error = True
        errorMsg += ",Please enter a username"
    elif len(username) < 3 or len(username) > 20:
        error = True
        errorMsg += ",Pleae enter a valid username"
    elif " " in username:
        error = True
        errorMsg += ",Pleae enter a valid username"

    if password == "":
        error = True
        errorMsg += ",Please enter a password"
    elif len(password) < 3 or len(password) > 20:
        error = True
        errorMsg += ",Pleae enter a valid password"
    elif " " in password:
        error = True
        errorMsg += ",Pleae enter a valid password"
    else:
        if confPassword != password:
            error = True
            errorMsg += ",Please confirm your password"

    if email != "":
        if "@" not in email or "." not in email or len(email) < 3 or len(email) > 20:
            error = True
            errorMsg += ",Please enter a valid email"


    if error == True:
        return redirect("/?error=" + errorMsg)
    else:
        body = jinja_env.get_template('login.html')
        return body.render()

app.run()