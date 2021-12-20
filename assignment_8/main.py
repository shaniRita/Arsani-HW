from flask import Flask, redirect, url_for,render_template
app = Flask(__name__)


@app.route('/cv1')
@app.route('/')
def c1():
    return render_template('cv1.html')
@app.route('/cv2')
def c2():
    return render_template('cv2.html')
@app.route('/cv11')
def c11():
    return render_template('cv11.html')

@app.route('/assignment8')
def music():
    print ("im in about ")
    name = 'shani'
    fname= 'freiman'
    return render_template('assignment8.html',
                           profile={'name':'shani','second_name':'freiman'},
                           university='BGU',
                           degree=['BSc','MS'],
                           hobbies=('art','music','sql'))
    return render_template('assignment8.html')


if __name__ == '__main__':
    app.run(debug=True)

