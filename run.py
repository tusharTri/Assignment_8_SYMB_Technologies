from API_APP import create_app,db
app=create_app()
app.app_context().push()
from flask import jsonify, request

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
    neighbours=db.relationship('CountryNeighbour', backref=('CountryModel'), lazy=True) 
    
    
class CountryNeighbour(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    country_id = db.Column(db.Integer, db.ForeignKey('CountryModel.id'), nullable=False)
    neighbour_country_id = db.Column(db.String,  nullable=False)
    
def rowToDict(country):
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
                return obj
 
@app.route('/country', methods=['GET','POST'])
def country():
        if request.method == 'GET':
                
                #IF QUERIES/FILTERS  APPLICABLE
                
                page = request.args.get('page',  type=int)
                limit = request.args.get('limit', type=int)
                name = request.args.get('name')
                region = request.args.get('region')
                sub_region = request.args.get('subregion')
                data = request.args.get('sort_by')
                
                sort_query = ''
                search_query=''
                
                if data == 'a_toz':sort_query = '(CountryModel.name)'
                elif data == 'z_toa':sort_query = '(CountryModel.name.desc())'
                elif data == 'population_high_to_low':sort_query = '(CountryModel.population)'
                elif data == 'population_low_to_high':sort_query = '(CountryModel.population.desc())'
                elif data == 'area_high_to_low':sort_query = '(CountryModel.area)'
                elif data == 'area_low_to_high':sort_query = '(CountryModel.area.desc())'

                if name:search_query += 'name=name,'
                if region:search_query += 'region=region,'
                if sub_region:search_query += 'subregion=sub_region'

                final_query = 'CountryModel.query'

                if search_query: final_query += f'.filter_by({search_query})' 
                if sort_query:   final_query += f'.order_by{sort_query}'
                


                final_query += f'.paginate(page={page}, per_page={limit})'
                countries = eval(final_query)
                
        
                #IF QUERIES/FILTERS NOT APPLICABLE and also continued for applicable
                
                # countries=CountryModel.query.all()
                displayCountries={}
                data={}
                listcountry=[]
                for country in countries:
                        obj=rowToDict(country)
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
                displayCountries={}
                data = {}
                displayCountries['message'] = 'Country List'
                country = CountryModel.query.filter_by(id=id).first()
                obj=rowToDict(country)
                data['country'] = obj
                displayCountries['data'] = data
                displayCountries['message']='Country List'
                return jsonify(displayCountries),201

@app.route('/country/<id>/neighbour')
def neighbour(id):
        if request.method == 'GET':
                displayCountries={}
                data={}
                listcountry=[]
                country = CountryModel.query.filter_by(id=id).first()
                
                for neighbour in country.neighbours:
                        neighbour=CountryModel.query.filter_by(id=neighbour.id).first()
                        obj=rowToDict(neighbour)
                        listcountry.append(obj)
                data['list']=listcountry
                displayCountries['data']=data
                displayCountries['message']='Country List'
                return jsonify(displayCountries)

if __name__ == '__main__':
    app.run(debug=True)