from flask import Flask, redirect, url_for
from flask import render_template

app = Flask(__name__)


@app.route('/Home')
@app.route('/')
def home_func():
    found = True
    if found:
        return redirect('/about')
    else:
        return redirect(url_for(home_func))


@app.route('/about')
def about_func():
    name = 'Shani'
    second_name = 'Rita'
    uni = 'BGU'
    return render_template('about.html',
                           profile={'name': 'Shani Freiman', 'Second_name': 'Rita'},
                           university=uni,
                           Degrees=['Bcs', 'MSc', 'GrandMaster'],
                           Hobbies=('art', 'music', 'sql'))


@app.route('/catalog')
def catalog_func():
    return "Welcome to the catalog page"


if __name__ == '__main__':
    app.run(debug=True)
