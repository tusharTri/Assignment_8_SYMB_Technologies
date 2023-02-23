from API_APP import create_app,db
app=create_app()
app.app_context().push()
from flask import jsonify
class CountryModel(db.Model):
    __tablename__='CountryModel'
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

@app.route('/country')
def get():
        countries=CountryModel.query.all()
        displayCountries={}
        data={}
        
        
        listcountry=[]
        for country in countries:
                listcountry.append(country.to_dict())
        data['country']=listcountry
        displayCountries['data']=data
        displayCountries['message']='Country List'
        return jsonify(displayCountries)
    
if __name__ == '__main__':
    app.run(debug=True)