{"filter":false,"title":"forms.py","tooltip":"/Web/app/forms.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":9,"column":120},"action":"insert","lines":["from wtforms import StringField","from flask_babelpkg import lazy_gettext","from wtforms.validators import DataRequired","from flask_appbuilder.fieldwidgets import BS3TextFieldWidget","from flask_appbuilder.forms import DynamicForm","","","class TestForm(DynamicForm):","    TestFieldOne = StringField(lazy_gettext('Test Field One'), validators=[DataRequired()], widget=BS3TextFieldWidget())","    TestFieldTwo = StringField(lazy_gettext('Test Field One'), validators=[DataRequired()], widget=BS3TextFieldWidget())"],"id":1}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":8,"column":56},"end":{"row":8,"column":56},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1540242703182,"hash":"dc5f74e8acd99acc21edf14b571c9c532fe0cca6"}