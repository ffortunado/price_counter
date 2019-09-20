from flask import render_template
from flask_admin import BaseView, expose

from app import app
from .models import CommercialProposal, MainMetrics
from app import db
from .form import CreateCommercialProposal


class AnalyticsView(BaseView):
    @expose('/')
    def index(self):
        form = CreateCommercialProposal()
        return self.render('create_cp.html', form=form)


@app.route('/')
@app.route('/index')
def index():
    user = {'username': '123'}
    return render_template('create_cp.html', title='title', user=user)


def save_commercial_proposal(domain, main_region, description, keywords):
    cp = CommercialProposal(domain=domain, main_region=main_region, description=description)
    db.session.add(cp)
    db.session.flush()
    db.session.refresh(cp)

    for kw in keywords:
        mm = MainMetrics(cp=cp, keyword=kw)
        db.session.add(mm)

    db.session.commit()
