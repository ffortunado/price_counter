from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import InputRequired

from .models import Region


def get_regions():
    return [(str(region.id), region.name) for region in Region.query.all()]


class CreateCommercialProposal(FlaskForm):

    domain = StringField('Домен <strong style="color: red">*</strong>',
                         validators=[InputRequired()],
                         render_kw={'class': 'form-control'})
    description = TextAreaField('Доп. инфо <strong style="color: red">*</strong>',
                                render_kw={'class': 'form-control'})
    main_region = SelectField('Главный регион', choices=get_regions(),
                              render_kw={'class': 'form-control'})
    keywords = TextAreaField('Список ключевиков',
                             render_kw={'class': 'form-control', 'rows': '10'})
