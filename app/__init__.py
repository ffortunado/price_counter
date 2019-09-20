from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView



app = Flask(__name__)
app.secret_key = 'secret_key'
app.config.from_object(Configuration)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from .models import CommercialProposal, MainMetrics


class MainMetricsView(ModelView):
    column_searchable_list = ['keyword']


admin = Admin(app, name='price_counter', template_mode='bootstrap3')
admin.add_views(ModelView(CommercialProposal, db.session), MainMetricsView(MainMetrics, db.session))


from app import views, models
