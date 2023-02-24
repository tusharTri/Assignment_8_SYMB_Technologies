from API_APP import create_app,db
app=create_app()
app.app_context().push()
from flask import jsonify, request
db.create_all()
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
    area =db.Column(db.Text,  nullable=False)
    map_url=db.Column(db.Text,  nullable=False) 
    population=db.Column(db.Text,  nullable=False)
    flag_url =db.Column(db.Text,  nullable=False) 
    
    
# class CountryNeighbour(db.Model):
#     id = db.Column(db.Integer, nullable=False, primary_key=True)
#     country_id = db.Column(db.Integer, db.ForeignKey('CountryModel.id'), nullable=False)
#     neighbour_country_id = db.Column(db.String,  nullable=False)
#     created_at = db.Column(db.String,  nullable=False)
#     updated_at = db.Column(db.String)

 
@app.route('/country', methods=['GET','POST'])
def country():
        if request.method == 'GET':
                countries=CountryModel.query.all()
                displayCountries={}
                data={}
                listcountry=[]
                for country in countries:
                        obj={}
                        obj["id"]=country.id,
                        obj["name"]=country.name,
                        obj["cca"]=country.cca,
                        obj["currency_code"]=country.currency_code,
                        obj["currency"]=country.currency,
                        obj["capital"]=country.capital,
                        obj["region"]=country.region ,
                        obj["subregion"]=country.subregion,
                        obj["area"]=country.area,
                        obj["map_url"]=country.map_url,
                        obj["population"]=country.population,
                        obj["flag_url"]=country.flag_url
                        
                        listcountry.append(obj)
                data['list']=listcountry
                displayCountries['data']=data
                displayCountries['message']='Country List'
                return jsonify(displayCountries)
        elif request.method == 'POST':
                data = request.form
                entry = CountryModel(id=data['id'], name=data['name'], cca=data['cca3'],
                                currency_code=data['currency_code'], currency=data['currency'], capital=data['capital'],
                                region=data['region'], subregion=data['subregion'],
                                area=data['area'],
                                map_url=data['map_url'], 
                                population=data['population'],
                                flag_url=data['flag_url'])

                db.session.add(entry)
                db.session.commit()
                return 'received', 201


@app.route('/country/<id>')
def countryById(id):
        if request.method == 'GET':
                countries=CountryModel.query.all()
                # id= countries[-1][id]+1
                displayCountries={}
                data = {}
                displayCountries['message'] = 'Country List'
                country = CountryModel.query.filter_by(id=id).first()
                obj={}
                obj["id"]=country.id,
                obj["name"]=country.name,
                obj["cca"]=country.cca,
                obj["currency_code"]=country.currency_code,
                obj["currency"]=country.currency,
                obj["capital"]=country.capital,
                obj["region"]=country.region ,
                obj["subregion"]=country.subregion,
                obj["area"]=country.area,
                obj["map_url"]=country.map_url,
                obj["population"]=country.population,
                obj["flag_url"]=country.flag_url
                
                        
                data['country'] = obj
                displayCountries['data'] = data
                displayCountries['message']='Country List'
                return jsonify(displayCountries),201

if __name__ == '__main__':
    app.run(debug=True)