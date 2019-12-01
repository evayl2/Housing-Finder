from flask import request, redirect
@app.route('/settings', methods = ['POST'])
def signup():
    email = request.form['Email']
    name = request.form['Name']
    major = request.form['Major']
    price = request.form['Desired Price']
    gender = request.form['Gender']
    year = request.form['Year']
    print("The email address of '" + name + " is '" + email)
    return redirect('/')
