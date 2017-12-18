# -*- coding: utf-8 -*-

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	SQLALCHEMY_TRACK_MODIFICATIONS = True
	# FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
	# FLASKY_MAIL_SENDER = ''
	# FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
	
	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG = True
	MAIL_SERVER = 'smtp.qq.com',
	MAIL_PROT = 25,
	MAIL_USE_TLS = True,
	MAIL_USE_SSL = False,
	MAIL_USERNAME = "3020546767",
	MAIL_PASSWORD = "kyf2014081608",
	MAIL_DEBUG = True
	# MAIL_SERVER = ''
	# MAIL_PORT = 587
	# MAIL_USE_TLS = True
	# MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
	# MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:223344@localhost:3306/test?charset=utf8'
	
	@staticmethod
	def init_app(app):
		pass

class TestingConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')

class ProductionConfig(Config):
	pass
	# SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
	# 	'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
'development': DevelopmentConfig,
'testing': TestingConfig,
'production': ProductionConfig,
'default': DevelopmentConfig
}