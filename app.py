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


@app.route('/favoritecourse')
def favoritecourse():
    print("enter course: " + request.args.get('course'))
    print("enter number: " + request.args.get('number'))
    return render_template('favoritecourse.html')


@app.route('/contact', methods=['GET'])
def contact():
    if request.method == 'POST':
        return render_template('contact.html', form_submitted = True)
    else:
        return render_template('contact.html')



if __name__ == '__main__':
    app.run()