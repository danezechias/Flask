from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello world from Dan Ouiya I am hading my first line of code'

@app.route('/hello')
def hello():
    return render_template('hello.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/nn')
def courses():
    fun_courses = ['32', '222', '222']
    return render_template('nn.html', courses = fun_courses )


@app.route('/favoritecourse', methods=['GET'])
def favoritecourse():
    if request.method == 'POST':
        print("favorite course: " + request.args.get('course'))
        print("favorite course number: " + request.args.get('number'))

    return render_template('favoritecourse.html')

@app.route('/contact', methods=['GET'])
def contact():
    if request.method == 'POST':
        print("enter firstname: " + request.args.get('firstname'))
        print("enter lastname: " + request.args.get('lastname'))
        print("enter email address: " + request.args.get('Email'))
        print("enter password: " + request.args.get('Password'))

    return render_template('contact.html', form_submitted = True)




















if __name__ == '__main__':
    app.run()