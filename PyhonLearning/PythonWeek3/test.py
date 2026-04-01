# Flask example
from flask import Flask , render_template , request , url_for , redirect , flash , session
app = Flask(__name__)
@app.route('/')
def home():
    return "<h1>Hello World - This should show!</h1>"

if __name__ == "__main__":
    app.run(debug=True)