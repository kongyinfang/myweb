from datetime import datetime
from flask import render_template, session, redirect, url_for
from .import users
# from ..forms import NameForm
from .. import db
from ..models import User

@user.route('/index')
def index():
	return render_template('user/index.html')

@user.route('/add/', methods=['GET', 'POST'])
def add():
	if request.method == 'POST':
		p_user = request.form.get('username', None)

		if not p_user:
			return 'input error'

		newobj = User(username=p_user)
		db.session.add(newobj)
		db.session.commit()
		users = User.query.all()
		return render_template('user/add.html', users=users)
	users = User.query.all()
	return render_template('user/add.html', users=users)

@user.route('/show')
def show():
	return 'user_show'
