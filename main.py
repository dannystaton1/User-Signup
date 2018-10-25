from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)


app = Flask(__name__)
app.config["DEBUG"] = True



@app.route("/")
def get_index():
    template = jinja_env.get_template("usersignup.html")
    return template.render()

@app.route("/", methods = ["POST"])
def form_index():

    username = request.form["username"]
    password = request.form["password"]
    email = request.form["email"]

    username_error = ""
    password_error = ""




app.run()
