from app import db


class Region(db.Model):
    __tanlename__ = 'region'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    yandex_code = db.Column(db.Integer, nullable=True)
    google_code = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return '<Region {}>'.format(self.name)


class CommercialProposal(db.Model):
    __tablename__ = 'commercial_proposal'

    id = db.Column(db.Integer, primary_key=True)
    domain = db.Column(db.String(64), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    main_region_id = db.Column(db.Integer, db.ForeignKey(Region.id), nullable=False)
    main_region = db.relationship(Region)

    def __repr__(self):
        return '{}, {}'.format(self.id, self.domain)


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
