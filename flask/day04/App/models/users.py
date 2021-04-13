from App.ext import models

class UsersModel(models.Model):

    id=models.Column(models.Integer,primary_key=True)
    name=models.Column(models.String(32))

    def save(self):
        models.session.create_all(self)
        models.session.commit()

