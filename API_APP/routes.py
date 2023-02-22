from API_APP.models import CountryModel
from API_APP import api
from flask_restful import Resource


class Country(Resource):
    countries=CountryModel.query.all()
    displayCountries={}
    for country in countries:
        displayCountries[country.id]={                
                "id": country.id,
                "name": country.name,
                "cca3": country.cca3,
                "currency_code": country.currency_code,
                "currency": country.currency,
                "capital": country.capital,
                "region":country.region ,
                "subregion": country.subregion,
                "area": country.area,
                "map_url": country.map_url,
                "population": country.polulation,
                "flag_url":country.flag_url
        }

api.add_resource(Country,'/country')
