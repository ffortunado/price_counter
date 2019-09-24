from time import sleep

from flask import render_template, request
from flask_admin import BaseView, expose

from .models import CommercialProposal, MainMetrics, Region
from app import db, app
from .form import CreateCommercialProposal
from .async_views import count_words, generate_tasks_by_id


class AnalyticsView(BaseView):
    @expose('/', methods=['GET', 'POST'])
    def index(self):
        if request.method == 'POST':
            form = CreateCommercialProposal(request.form)
            if form.validate_on_submit():
                cp_id = None
                kw_ids = []
                cp = CommercialProposal(domain=request.form.get('domain'),
                                        description=request.form.get('description'),
                                        main_region=Region.query.get(int(request.form.get('main_region'))))
                db.session.add(cp)
                db.session.flush()
                cp_id = cp.id
                keywords = request.form.get('keywords')
                for kw in [k.strip() for k in keywords.split('\n') if k]:
                    mm = MainMetrics(cp=cp, keyword=kw)
                    db.session.add(mm)
                    db.session.flush()
                    kw_ids.append(mm.id)
                db.session.commit()
                generate_tasks_by_id(cp_id, kw_ids)

        form = CreateCommercialProposal()
        count_words.delay()
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
