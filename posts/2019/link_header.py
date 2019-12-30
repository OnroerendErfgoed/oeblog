# -*- coding: utf-8 -*-
import requests

# Our endpoints
INVENTARIS = 'https://inventaris.onroerenderfgoed.be'
AFBEELDINGEN = 'https://beeldbank.onroerenderfgoed.be/images'
ERFGOEDOBJECTEN = INVENTARIS + '/erfgoedobjecten'
AANDUIDINGSOBJECTEN = INVENTARIS + '/aanduidingsobjecten'
THEMAS = INVENTARIS + '/themas'

def get_data(url, parameters):
    '''
    Fetch all data from a url until there are no more `next` urls in the Link
    header.

    :param str url: The url to fetch from
    :param dict parameters: A dict of query string parameters
    :rtype: dict
    '''
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
MUNICIPALITY_ID = 191

# Fetch all data
afbeeldingen = get_data(AFBEELDINGEN, {'municipality': MUNICIPALITY_ID})
erfgoedobjecten = get_data(ERFGOEDOBJECTEN, {'gemeente': MUNICIPALITY_ID})
aanduidingsobjecten = get_data(AANDUIDINGSOBJECTEN, {'gemeente': MUNICIPALITY_ID})
themas = get_data(THEMAS, {'gemeente': MUNICIPALITY_ID})

# Add everything together
stuff = afbeeldingen + erfgoedobjecten + aanduidingsobjecten + themas

# Print the URIs of all objects involved
uris = [thing['uri'] for thing in stuff]
print(uris)
