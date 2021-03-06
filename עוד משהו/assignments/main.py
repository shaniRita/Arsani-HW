from flask import Flask, redirect, url_for,render_template,request , session
app = Flask(__name__)
app.secret_key = '12345'

users = {'user1': {'name': 'shani', 'email': 'shani@gmail.com'},
         'user2': {'name': 'itamar', 'email': 'itamar@gmail.com'},
         'user3': {'name': 'shay', 'email': 'shay@gmail.com'},
         'user4': {'name': 'agam', 'email': 'agam@gmail.com'},
         'user5': {'name': 'eden', 'email': 'eden@gmail.com'},
         'user6': {'name': 'coral', 'email': 'coral@gmail.com'}
         }

@app.route('/cv1')
def c1():
    return render_template('cv1.html')

@app.route('/')
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


@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9_func():
    print(users.values())

    if request.method == 'GET':
        if session['username']:
          if 'search' in request.args:
            search = request.args['search']
            return render_template('assignment9.html', username=session['username'], search=search, users=users)
        return render_template('assignment9.html', users=users)

    if request.method == 'POST':
        #DB
        username = request.form['username']
        Password = request.form['password']
        found = True
        if found:
            session['username'] = request.form['username']
            session['user_login'] = True
            return render_template('assignment9.html', username=username, users=users)
        else:
            return render_template('assignment9.html')


@app.route('/logout')
def logout_func():
    session['username'] = '' ##Log out excist user
    return render_template('assignment9.html')
if __name__ == '__main__':
    app.run(debug=True)

