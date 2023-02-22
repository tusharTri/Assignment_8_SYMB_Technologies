
from API_APP import db

class CountryModel(db.Model):
    id=db.Column(db.Text,  nullable=False, primary_key=True) 
    name=db.Column(db.Text,  nullable=False) 
    cca=db.Column(db.Text,  nullable=False)
    currency_code=db.Column(db.Text,  nullable=False)
    currency=db.Column(db.Text,  nullable=False) 
    capital=db.Column(db.Text,  nullable=False)
    region=db.Column(db.Text,  nullable=False) 
    subregion=db.Column(db.Text,  nullable=False) 
    area =db.Column(db.Numeric,  nullable=False)
    map_url=db.Column(db.Text,  nullable=False) 
    population=db.Column(db.Numeric,  nullable=False)
    flag_url =db.Column(db.Text,  nullable=False) 
    created_at= db.Column(db.Text,  nullable=False) 
    updated_at =db.Column(db.Text,  nullable=False) 
   
