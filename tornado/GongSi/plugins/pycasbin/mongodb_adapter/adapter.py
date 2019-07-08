import casbin
from mongoengine import Document
from mongoengine import connect
from mongoengine.fields import IntField,StringField,UUIDField



class CasbinRule(Document):

    __tablename__="casbin_rule"

    id=IntField(required=True,parmary_key=True,unique=True)
    ptype=StringField(required=True,max_length=255)
    v0=StringField(max_length=255)
    v1=StringField(max_length=255)
    v2=StringField(max_length=255)
    v3=StringField(max_length=255)
    v4=StringField(max_length=255)
    v5=StringField(max_length=255)
    v6=StringField(max_length=255)

    def __str__(self):
        text=self.ptype

        if self.v0:
            text=text+','+self.v0
        if self.v1:
            text=text+','+self.v1
        if self.v2:
            text=text+','+self.v2
        if self.v3:
            text=text+','+self.v3
        if self.v4:
            text=text+','+self.v4
        if self.v5:
            text=text+','+self.v5
        if self.v6:
            text=text+','+self.v6
        
        return text
    
    def __repr__(self):
        return '<CasbinRule {}:"{}">'.format(self.id,str(self))


if __name__ == "__main__":
    rule=CasbinRule()
    rule.ptype='g'
    rule.v0='superadmin'
    rule.v1='index'
    rule.v2='get'
