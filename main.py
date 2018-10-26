from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)


app = Flask(__name__)
app.config["DEBUG"] = True



@app.route("/")
def sign_up_form():
    template = jinja_env.get_template("usersignup.html")
    return template.render()

@app.route("/", methods = ["POST"])
def form_complete():
    
 
    username = request.form["username"]
    password = request.form["password"]
    verfiy_password = request.form["verfiy_password"]
    email = request.form["email"]
    
    
    
    username_error = ""
    password_error = ""
    verfiy_password_error = ""
    email_error = ""


    field_error = "Required field"
    user_pass_error = "Invaild, must contain no spaces."
    invaild_password = "Please re-enter password."
    count = "Must be between 3 to 20 characters."

def value(x):
    if x:
        return True
    else:
        return False
def value_length(x):
      if len(x) > 2 and len(x) < 21:
        return True
    else:
        return False

def email(x): 
    if x.comt("@") >= 1:
        return True
    else:
        return False

def email_2(x):
    if x.count("@") <=1:
        return True
    else:
        return False

def email_period(x):
    if x.comt(".") >= 1:
        return True
    else:
        return False

def email_periods(x):
    if x.count(".") <=1:
        return True
    else:
        return False 
        





app.run()
