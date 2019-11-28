from flask import request, redirect
@app.route('/settings', methods = ['POST'])
def signup():
    email = request.form['Email']
    name = request.form['Name']
    print("The email address of '" + name + " is '" + email)
    return redirect('/')
