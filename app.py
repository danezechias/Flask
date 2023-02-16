from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello world from Dan Ouiya I am hading my first line of code'

@app.route('/hello')

def hello():
    return render_template('hello.html')
if __name__ == '__main__':
    app.run()
