# -*- coding: utf-8 -*-
import requests

INVENTARIS = 'https://inventaris.onroerenderfgoed.be'
AFBEELDINGEN = 'https://beeldbank.onroerenderfgoed.be/images'
INFOCAT = 'https://bib.onroerenderfgoed.be/werken'
ERFGOEDOBJECTEN = INVENTARIS + '/erfgoedobjecten'
AANDUIDINGSOBJECTEN = INVENTARIS + '/aanduidingsobjecten'
THEMAS = INVENTARIS + '/themas'

def get_data(url, parameters):
    data = []

    headers = {'Accept': 'application/json'}

    res = requests.get(url, params=parameters, headers=headers)

    data.extend(res.json())

    while 'next' in res.links:
        res = requests.get(res.links['next']['url'], headers=headers)
        data.extend(res.json())

    return data

# Determine the CRAB ID for the gemeente you want
# https://loc.geopunt.be/v4/Location?q=knokke-heist

afbeeldingen = get_data(AFBEELDINGEN, {'municipality': 191})
erfgoedobjecten = get_data(ERFGOEDOBJECTEN, {'gemeente': 191})
aanduidingsobjecten = get_data(AANDUIDINGSOBJECTEN, {'gemeente': 191})
themas = get_data(THEMAS, {'gemeente': 191})

stuff = afbeeldingen + erfgoedobjecten + aanduidingsobjecten + themas

uris = [thing['uri'] for thing in stuff]
print(uris)
