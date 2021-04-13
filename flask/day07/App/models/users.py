from App.ext import db

class UsersModel(db.Model):

    __tablename='users'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(22))

    def save(self):
        db.create_all()


