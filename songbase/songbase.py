from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    # how to get form data is different for GET vs. POST
    if request.method =="GET":
        # return "Hello GET"
        return render_template('form.html')
    if request.method == "POST":
        first_name = request.form["first_name"]
        # return "hi, your name is %s" % first_name
        return render_template('form.html', first_name=first_name)


@app.route('/users/<string:username>')
def users(username):
     return render_template('user.html', uname=username)


@app.route('/user')
def user():
    return "this is the page for users"



if __name__ == '__main__':
    app.run()
