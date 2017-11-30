from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/welcome', methods=['POST'])
def welcome():
    username = request.form['user-id']
    password = request.form['users-password']
    valid_pass = request.form['verify-password']
    email = request.form['users-email']
    
    error = ""
    error2 = ""
    error3 = ""
    error4 = ""

    if len(username) < 3 or len(username) > 20 :
        error = "That's not a valid username"
  
    if len(password) < 3 or len(password) > 20 :
        error2 = "That's not a valid password"
    
    if len(valid_pass) < 3 or len(valid_pass) > 20:
        error3 = "Passwords do not match"
        if  valid_pass != password:
            error3 = "Passwords do not match"

    if len(email) >= 1:
        if len(email) < 3 or len(email) > 30:
            error4 = "Please provide a valid email"
            if not '@' and not '.' in email:
                error4 = "Please provide a valid email"

    if not error and not error2 and not error3 and not error4:
        
        return render_template("welcome.html", username = username)
    

    else: 
        return render_template("edit.html",username=username, email=email, error=error, error2=error2, error3=error3, error4=error4)

@app.route('/')
def index():
    error = request.args.get('error')
    error2 = request.args.get('error2')
    error3 = request.args.get('error3')
    error4 = request.args.get('error4')
    username = request.args.get('username')
    email = request.args.get('email')

    return render_template("edit.html",username=username, email=email, error=error, error2=error2, error3=error3, erro4=error4)

app.run()