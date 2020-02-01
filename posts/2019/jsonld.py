# -*- coding: utf-8 -*-
import requests
from pyld import jsonld
import json

# Add everything together and transform to linked data
inventaris_context = {
    "dct": "http://purl.org/dc/terms/",
    "naam": "dct:title",
    "korte_beschrijving": "dct:description",
    "uri": "@id"
}

dct_context = {
    "dct": "http://purl.org/dc/terms/",
    "title": "dct:title",
    "description": "dct:description",
    "uri": "@id"
}

es = {
    '@context': inventaris_context,
    '@graph':
    [{
        'naam': 'Diephuis',
        'uri': 'https://id.erfgoed.net/erfgoedobjecten/1',
        'korte_beschrijving': 'Mijn diephuis is een diephuis, maar soms ook een \
        brede woning.'
    }, {
        'naam': 'Broodhuis',
        'uri': 'https://id.erfgoed.net/erfgoedobjecten/2',
        'korte_beschrijving': 'Een broodhuis is de woning van een bakker.'
    }]
}

e = {
    'naam': 'Diephuis',
    'uri': 'https://id.erfgoed.net/erfgoedobjecten/1',
    'korte_beschrijving': 'Mijn diephuis is een diephuis, maar soms ook een \
    brede woning.'
}

print(e)
expanded = jsonld.expand(e,{'expandContext':inventaris_context})
print(expanded)

print(jsonld.compact(expanded, dct_context))
