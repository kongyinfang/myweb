# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, redirect, url_for, request

from test import db

from test import User
user = Blueprint('user', __name__)

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

