# -*- coding: utf-8 -*-

from test import app
from user import user

app.register_blueprint(user, url_prefix='/user')