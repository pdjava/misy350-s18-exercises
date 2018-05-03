from flask import Flask, render_template
app = Flask(__name__)
import random

 # greeting_list = ['Ciao', 'Hai', 'Salut', 'Nihao']
# print random.choice(greeting_list)


@app.route('/')
def index():
    #"hello World"
    return render_template('index.html')     # 'Hello Priyanka'



## dynamic content based on the page
@app.route('/users/<string:uname>')
def users(uname):
    # return "hello %s" % username
    return render_template('user.html', uname=uname)


    @app.route('/user')
    def user():
        return "this is the page for users"


    #@app.route('/hello')
    # def user():
        # return print


if __name__ == '__main__':
    app.run() # debug = TRUE && host = '0.0.0.0', port = 4500
