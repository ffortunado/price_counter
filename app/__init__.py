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
from .views import AnalyticsView


class MainMetricsAdmin(ModelView):
    column_searchable_list = ['keyword']


class CommercialProposalAdmin(ModelView):
    column_display_pk = True


admin = Admin(app, name='price_counter', template_mode='bootstrap3')
admin.add_views(CommercialProposalAdmin(CommercialProposal, db.session),
                MainMetricsAdmin(MainMetrics, db.session),
                AnalyticsView(name='Создать КП', endpoint='create_cp'))


from app import views, models
