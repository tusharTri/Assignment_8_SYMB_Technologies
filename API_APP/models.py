
from API_APP import db

class CountryModel(db.Model):
    __tablename__='CountryModel'
    id=db.Column(db.Integer,  nullable=False, primary_key=True) 
    name=db.Column(db.Text,  nullable=False) 
    cca=db.Column(db.Text,  nullable=False)
    currency_code=db.Column(db.Text,  nullable=False)
    currency=db.Column(db.Text,  nullable=False) 
    capital=db.Column(db.Text,  nullable=False)
    region=db.Column(db.Text,  nullable=False) 
    subregion=db.Column(db.Text,  nullable=False) 
    area =db.Column(db.Text,  nullable=False)
    map_url=db.Column(db.Text,  nullable=False) 
    population=db.Column(db.Text,  nullable=False)
    flag_url =db.Column(db.Text,  nullable=False)
    neighbours=db.relationship('CountryNeighbour', backref=('CountryModel'), lazy=True) 
    
    
class CountryNeighbour(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    country_id = db.Column(db.Integer, db.ForeignKey('CountryModel.id'), nullable=False)
    neighbour_country_id = db.Column(db.String,  nullable=False)
    