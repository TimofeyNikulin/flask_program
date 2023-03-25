from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class JobForm(FlaskForm):
    team_leader = StringField('Тим-лидер (ID)', validators=[DataRequired()])
    job = StringField('Название работы', validators=[DataRequired()])
    work_size = StringField('Размер работы (в часах)',
                            validators=[DataRequired()])
    collaborators = StringField('Работники (ID)', validators=[DataRequired()])
    is_finished = BooleanField(
        'Работа окончится?', validators=[DataRequired()])
    submit = SubmitField('Войти')
