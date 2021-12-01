from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/Home')
@app.route('/')
def hello_func():
    return 'Welcome to the Home Page'

@app.route('/about', methods=['GET'])
def about_func():
    # TODO
    # DO SOMETHING WITH DB
    print('About page')
    return 'WELCOME TO ABOUT'


@app.route('/catalog')
def catalog_func():
    return 'Welcome to Catalog page'

if __name__ == '__main__':
    app.run(debug=True)

