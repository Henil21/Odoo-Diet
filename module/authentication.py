from module import app
from module import db, User
from flask import render_template, url_for, request, redirect, session

# Password hashing
import bcrypt

# Password strength Verification
from zxcvbn import zxcvbn

@app.route('/home', methods=["GET", "POST"])
def home():
    if 'username' in session:
        return render_template('index.html')
    return redirect('/signin')

@app.route('/', methods=["GET", "POST"])
@app.route('/signin', methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.checkpw(password.encode('utf-8'), user.password):
            session['username'] = user.username
            # return redirect('/dashboard')
            return redirect('/home')
        if not user:
            return render_template('signin.html', msg="User does not exists.")
        if user and user.password != password:
            return render_template('signin.html', msg="Incorrect Password")

    return render_template('signin.html')


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        iusername = request.form.get("username")
        ipassword = request.form.get("password")
        icpassword = request.form.get("cpassword")
        user = User.query.filter_by(username=iusername).first()
        if user:
            return render_template('signup.html', msg="User already exists")
        if zxcvbn(ipassword)["score"] < 2:
            return render_template('signup.html', msg=f"{zxcvbn(ipassword)['feedback']['warning']}")
        if ipassword == icpassword:
            # Generating hashed Password
            # salt = bcrypt.gensalt()
            hashPassword = bcrypt.hashpw(ipassword.encode('utf-8'), bcrypt.gensalt())

            user = User(username=iusername,
                        password=hashPassword)
            db.session.add(user)
            db.session.commit()
            # alldata = Table.query.all()
            # print(alldata)
            print(user)
            return redirect(url_for('signin'))
        else:
            return render_template('signup.html', msg="Password does not match.")
    return render_template('signup.html')


@app.route('/logout')
def logout():
    session.pop('username')
    return redirect('/signin')
