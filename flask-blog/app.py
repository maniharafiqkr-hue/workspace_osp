from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return "<h1>Welcome to My Flask Blog!</h1>"

if __name__ == '__main__':
    app.run(debug=True)
    

@app.route('/about')
def about():
    return "<h2>About This Blog</h2><p>This is a project for OSP.</p>"