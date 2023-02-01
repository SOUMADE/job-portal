from config import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(200),nullable=False)
    addDetailsUser=db.relationship('AddDetailsUser',backref='user')
    applicants = db.relationship('Applicants',backref='user')
    availablejobs = db.relationship('Availablejobs',backref='user')
    jobappliedbyuser = db.relationship('Jobappliedbyuser',backref='user')
    postedjobs = db.relationship('Postedjobs',backref='user')
    postInternships=db.relationship('PostInternships',backref='user')
    applyInternships=db.relationship("ApplyInternships",backref='user')
