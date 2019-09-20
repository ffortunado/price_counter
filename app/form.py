from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired


class CreateCommercialProposal(FlaskForm):
    domain = StringField('Домен <strong style="color: red">*</strong>',
                         validators=[InputRequired()],
                         render_kw={'class': 'form-control'})
    description = TextAreaField('Доп. инфо <strong style="color: red">*</strong>',
                                render_kw={'class': 'form-control'})
    main_region = StringField('Главный регион <strong style="color: red">*</strong>',
                              render_kw={'class': 'form-control'})
    kwords = TextAreaField('Список ключевиков',
                           render_kw={'class': 'form-control', 'rows': '10'})
