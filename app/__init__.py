from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from celery import Celery


def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


app = Flask(__name__)
app.config.from_object(Configuration)
celery = make_celery(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from .models import CommercialProposal, MainMetrics, Region
from .views import AnalyticsView


class MainMetricsAdmin(ModelView):
    column_searchable_list = ['keyword']


class CommercialProposalAdmin(ModelView):
    column_display_pk = True


admin = Admin(app, name='price_counter', template_mode='bootstrap3')
admin.add_views(CommercialProposalAdmin(CommercialProposal, db.session),
                MainMetricsAdmin(MainMetrics, db.session),
                ModelView(Region, db.session),
                AnalyticsView(name='Создать КП', endpoint='create_cp'),)


from app import views, models
