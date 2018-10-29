from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)


app = Flask(__name__)
app.config["DEBUG"] = True



@app.route("/", methods = ["GET"])
def sign_up_form():
   
    return render_template("usersignup.html")




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



def email_address(x): 
    if x.count("@") >= 1:
        return True
    else:
        return False



def email_2(x):
    if x.count("@") <=1:
        return True
    else:
        return False



def email3(x):
    if x.count(".") >= 1:
        return True
    else:
        return False


def email_periods(x):
    if x.count(".") <=1:
        return True
    else:
        return False


@app.route("/", methods = ["POST"])
def form_complete():
    
 
    username = request.form['username']
    password = request.form['password']
    verify_password= request.form['verify_password']
    email = request.form['email']
    
    
    
    username_error = ""
    password_error = ""
    verify_passwrod_error = ""
    email_error = ""


    field_error = "Required field"
    user_pass_error = "Invaild, must contain no spaces."
    invaild_password = "Please re-enter password."
    count = "Must be between 3 to 20 characters."


    if not value(password):
        password_error = field_error
        password = ''
        verify_password= ''
   
   
   
    elif not value_length(password):
        password_error = "Password " + count
        password = ''
        verify_password= ''
        verify_passwrod_error = invaild_password
   
   
   
    else:
        if " " in password:
            password_error = "Password " + user_pass_error
            password = ''
            verify_password= ''
            verify_passwrod_error = invaild_password

  

    if verify_password!= password:
        verify_passwrod_error = "Passwords must match"
        password = ''
        verify_password= ''
        password_error = 'Passwords must match'
            


    if not value(username):
        username_error = field_error
        password = ''
        verify_password= ''
        password_error = invaild_password
        verify_passwrod_error = invaild_password
   
   
   
   
    elif not value_length(username):
        username_error = "Username " + count
        password = ''
        verify_password= ''
        password_error = invaild_password
        verify_passwrod_error = invaild_password
   
   
   
    else:
        if " " in username:
            username_error = "Username " + user_pass_error
            password = ''
            verify_password= ''
            password_error = invaild_password
            verify_passwrod_error = invaild_password

  

   
    if value(email):

        if not value_length(email):
            email_error = "Email " + count
            password = ''
            verify_password= ''
            password_error = invaild_password
            verify_passwrod_error = invaild_password
        
        
        
        elif not email_address(email):
            email_error = "Email must contain the @ symbol"
            password = ''
            verify_password= ''
            password_error = invaild_password
            verify_passwrod_error = invaild_password
        
        
        elif not email_2(email):
            email_error = "Email must contain only one @ symbol"
            password = ''
            verify_password= ''
            password_error = invaild_password
            verify_passwrod_error = invaild_password
        
        
        
        elif not email3(email):
            email_error = "Email must contain ."
            password = ''
            verify_password= ''
            password_error = invaild_password
            verify_passwrod_error = invaild_password
        
        
        elif not email_periods(email):
            email_error = "Email must contain only one ."
            password = ''
            verify_password= ''
            password_error = invaild_password
            verify_passwrod_error = invaild_password
        
        
        
        
        else:
            if " " in email:
                email_error = "Email " + user_pass_error
                password = ''
                verify_password= ''
                password_error = invaild_password
                verify_passwrod_error = invaild_password

    
    if not username_error and not password_error and not verify_passwrod_error and not email_error:
        
        username = username
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template("usersignup.html", username_error=username_error, username=username, password_error=password_error, password=password,verify_passwrod_error=verify_passwrod_error, verify_password=verify_password, email_error=email_error, email=email)  


@app.route("/welcome", methods=['GET', 'POST'])
def welcome():

    username = request.args.get("username")
    return render_template("welcome_page.html", username=username)




app.run()
