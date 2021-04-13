from App.ext import db


class BlogModel(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(22))
    __tablename__='blog'

    def save(self):
        db.create_all()