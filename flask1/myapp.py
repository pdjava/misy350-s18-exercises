from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return "Hello Priyanka"


@app.route('/hello')
def hello():
    import random
    greeting_list = ['Ciao', 'Hai', 'Salut', 'Nihao']
    return random.choice(greeting_list)


if __name__ == '__main__':
    app.run()
