from datetime import datetime
from flask import flash, render_template, session, redirect, url_for, request
from . import main
from .forms import NameForm
from .. import db
from ..models import User



@main.route('/', methods=['GET', 'POST'])
def index():
	name = None
	form = NameForm()
	if form.validate_on_submit():
		old_name = session.get('name')
		if old_name is not None and old_name != form.name.data:
			flash('Looks like you have changed your name!')
		session['name'] = form.name.data
		return redirect(url_for('main.index'))
	# return render_template('index.html', form=form, name=session.get('name'))
	return render_template('index.html',
							form=form, name=session.get('name'),
							known=session.get('known', False),
							current_time=datetime.utcnow())

@main.route('/add/', methods=['GET', 'POST'])
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