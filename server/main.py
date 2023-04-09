from flask import Flask, render_template, request, redirect, url_for
from db import check_login_pass_in_db, select_name_nick
import config

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username)
        passwd = check_login_pass_in_db(username)
        
        if password == passwd:
            return redirect(url_for('user_page', username=username))
        else:
            return "Wrong data, try again."
    return render_template('login1.html')

@app.route('/user_page/<username>')
def user_page(username):
    result = select_name_nick(username)
    name = result[0][0]
    nickname = result[0][1]
    photo = f"http://{ config.host }:{ config.port }/static/images/{ username }_image.jpg"
    return render_template('user_page.html', username=username, photo_path=photo, name=name, nickname=nickname)

if __name__ == '__main__':
    app.run(debug=True)