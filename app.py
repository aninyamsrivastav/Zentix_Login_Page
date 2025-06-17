from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    if email == "test@zentix.com" and password == "1234":
        return redirect(url_for('dashboard'))  # FIXED: use function name, not .html
    else:
        return "<h1>Invalid Credentials</h1>"

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)