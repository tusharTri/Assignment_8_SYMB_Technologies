# from API_APP.models import CountryModel
# from flask import Blueprint
# from flask import Flask, jsonify

# main = Blueprint('main', __name__)

# from API_APP import db

# @main.route('/country')
# def get():
#         countries=CountryModel.query.all()
#         displayCountries={}
#         data={}
        
#         displayCountries['message']='Country List'
#         listcountry=[]
#         for country in countries:
#                 listcountry.append(country.to_dict())
#         data['list']=listcountry
#         displayCountries['data']=data
#         return (displayCountries)
        
#         # for country in countries:
#                 # displayCountries[country.id]={                
#                 #         "id": country.id,
#                 #         "name": country.name,
#                 #         "cca3": country.cca3,
#                 #         "currency_code": country.currency_code,
#                 #         "currency": country.currency,
#                 #         "capital": country.capital,
#                 #         "region":country.region ,
#                 #         "subregion": country.subregion,
#                 #         "area": country.area,
#                 #         "map_url": country.map_url,
#                 #         "population": country.polulation,
#                 #         "flag_url":country.flag_url
#                 # }
        
        
#         # if request.method=='POST':
#         #         id: countries[-1]['id']+1
#         #         name: request.form['name']
#         #         cca3: request.form['cca3']
#         #         currency_code: request.form['currency_code']
#         #         currency: request.form['currency']
#         #         capital: request.form['capital']
#         region:request.form['region']
#         #         subregion: request.form['subregion']
#         #         area: request.form['area']
#         #         map_url: request.form['map_url']
#         #         population: request.form['population']
#         #         flag_url:request.form['flag_url']
                           
#         #         new_obj={
#         #                 "id": id,
#         #                 "name": name,
#         #                 "cca3": cca3,
#         #                 "currency_code": currency_code,
#         #                 "currency": currency,
#         #                 "capital": capital,
#         #                 "region":region ,
#         #                 "subregion": subregion,
#         #                 "area": area,
#         #                 "map_url": map_url,
#         #                 "population": population,
#         #                 "flag_url":flag_url
#         #         }
#         #         countries.append(new_obj)
#         #         return jsonify(countries),201
        
        


