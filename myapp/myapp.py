from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    #"hello World"
    return render_template('index.html')


@app.route('/form')
def form():
    #"hello World"
    return render_template('form.html')


@app.route('/users/<string:username>/')
def users(username):
    #"hello World"
    return render_template('users.html',uname=username)


if __name__ == '__main__':
    app.run() # debug = TRUE && host = '0.0.0.0', port = 4500
