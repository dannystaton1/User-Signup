from flask import Flask, request
import cgitb
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

cgibt.enable()

app = Flask(__name__)
app.comfig["DEBUG"] = True



@app.route("/")