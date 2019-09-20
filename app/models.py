from app import db


class CommercialProposal(db.Model):
    __tablename__ = 'commercial_proposal'

    id = db.Column(db.Integer, primary_key=True)
    domain = db.Column(db.String(64), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    main_region = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<CommercialProposal {}, {}>'.format(self.domain, self.description)


class MainMetrics(db.Model):
    __tanlename__ = 'main_metrics'

    id = db.Column(db.Integer, primary_key=True)
    cp_id = db.Column(db.Integer, db.ForeignKey(CommercialProposal.id), nullable=False)
    cp = db.relationship(CommercialProposal)
    group = db.Column(db.Integer, nullable=True)
    keyword = db.Column(db.String(150), nullable=False)
    ws = db.Column(db.Integer, nullable=True)
    ws_accurate = db.Column(db.Integer, nullable=True)
    frequency = db.Column(db.String(5), nullable=True)
    rivalry = db.Column(db.Integer, nullable=True)
    commercial = db.Column(db.Integer, nullable=True)
    geo_dependent = db.Column(db.Boolean, nullable=True)
    vital = db.Column(db.Boolean, nullable=True)
    count_coldun = db.Column(db.Integer, nullable=True)
    main_page_top10 = db.Column(db.Integer, nullable=True)
    monthly_conversion = db.Column(db.Integer, nullable=True)
    price_for_click = db.Column(db.Float, nullable=True)
    advertiser = db.Column(db.Integer, nullable=True)
    capacity = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return '<MainMetrics {}>'.format(self.keyword)
