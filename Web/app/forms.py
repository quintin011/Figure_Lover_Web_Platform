from wtforms import StringField
from flask_babelpkg import lazy_gettext
from wtforms.validators import DataRequired
from flask_appbuilder.fieldwidgets import BS3TextFieldWidget
from flask_appbuilder.forms import DynamicForm


class TestForm(DynamicForm):
    TestFieldOne = StringField(lazy_gettext('Test Field One'), validators=[DataRequired()], widget=BS3TextFieldWidget())
    TestFieldTwo = StringField(lazy_gettext('Test Field One'), validators=[DataRequired()], widget=BS3TextFieldWidget())

class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Please use a different username.')