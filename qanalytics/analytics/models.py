from qanalytics.data import CRUDMixin, db

class Site(CRUDMixin, db.Model):
  __tablename__ = 'analytics_site'
  
  base_url = db.Column(db.String)
  visits = db.relationship('Visit', backref='site', lazy='select')
  user_id = db.Column(db.Integer, db.ForeignKey('users_user.id'))

  def __repr__(self):
    return '<site {:d} {}>'.format(self.id, self.base_url)
  
  def __str__(self):
    return self.baseurl
  
class Visit(CRUDMixin, db.Model):
  __tablename__ = 'analytics_visit'
  
  browser = db.Column(db.String)
  date = db.Column(db.DateTime)
  event = db.Column(db.String)
  url = db.Column(db.String)
  ip_address = db.Column(db.String)
  location = db.Column(db.String)
  lattitude = db.Column(db.Numeric)
  longitude = db.Column(db.Numeric)
  site_id = db.Column(db.Integer, db.ForeignKey('analytics_site.id'))
  
  def __repr__(self):
    r = '<visits for site id {:d}: {} - {:%Y-%m-%d %H:%M:%S}>'
    return r.format(self.site_id, self.url, self.date)
  
 