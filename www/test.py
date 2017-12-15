# -*- coding: utf-8 -*-

import os
from flask import Flask, flash
from flask import request, render_template
from flask import abort
from flask import url_for, redirect, session

from flask.ext.bootstrap import Bootstrap
# ...

from flask.ext.sqlalchemy import SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))


from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
class NameForm(Form):
	name = StringField('What is your name?', validators=[Required()])
	submit = SubmitField('Submit')




app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:223344@localhost:3306/test?charset=utf8'
#'sql:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)


class Role(db.Model):
	__tablename__ = 'roles'
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(64), unique=True)
	users = db.relationship('User', backref = 'role')


class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(64), unique=True, index = True)
	role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

	def __repr__(self):
		return '<User %r>' %self.username 


bootstrap = Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def index():
	name = None
	form = NameForm()
	if form.validate_on_submit():
		old_name = session.get('name')
		if old_name is not None and old_name != form.name.data:
			flash('Looks like you have changed your name!')
		session['name'] = form.name.data
		return redirect(url_for('index'))
	return render_template('index.html', form=form, name=session.get('name'))

@app.route('/index/<name>')
def indexname(name):
	return render_template('user.html', name=session.get('name'))

# @app.route('/')
# def index():
# 	# user_agent = request.headers.get('User-Agent')
# 	# return '<p>Your browser is %s</p>' % user_agent
# 	return render_template('index.html')

import views


# app.config['MAIL_SERVER'] 
# #初始化flask-mail

# from flask.ext.mail import Mail 
# mail = Mail(app)

