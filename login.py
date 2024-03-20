from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/authenticate', methods=['POST'])
def authenticate():
    username = request.form['username']
    password = request.form['password']
    
    # Here you can add your logic for authentication
    # For demonstration purposes, let's just print the username and password
    print("Username:", username)
    print("Password:", password)
    
    # Redirect to a success page or display a message
    return redirect(url_for('success'))

@app.route('/success')
def success():
    return "Login successful!"

if __name__ == '__main__':
    app.run(debug=True)
