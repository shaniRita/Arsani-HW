from flask import Flask
app = Flask(__name__)

@app.route('/Home')
@app.route('/')
def hello_func():
    return 'Welcome to the Home Page'

@app.route('/about')
def about_func():
    return 'Welcome to about page'


@app.route('/catalog')
def catalog_func():
    return 'Welcome to catalog page'

if __name__ == '__main__':
    app.run(debug=True)

