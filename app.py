from flask import Flask, render_template, request  # Import Flask

app = Flask(__name__)  # Create an app


@app.route('/')  # Define what happens at the homepage
def home():
    return "Welcome to my website!"  # Send back a response

@app.route('/about')  # Define what happens at the homepage
def about():
    return "This is the about url!"

@app.route('/greet/<name>')  # Define what happens at the homepage
def greet(name):
    return f"Hello {name}"

@app.route('/contact')
def contact():
    return render_template("contact.html")  

@app.route('/form')
def form():
    return render_template("form.html")  

@app.route('/form_submit', methods=['POST'])
def form_submit():
    print(request)
    fname = request.form['fname']
    return f"Hello, {fname}! Nice to meet you."


if __name__ == '__main__':
    app.run(debug=True, port=8080)  # Start the server
