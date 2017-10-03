# -*- coding: utf-8 -*-
import os
import json
import requests
from static_map_generator.generator import Generator


with open(os.path.join(os.path.dirname(__file__), 'Edegem.json'), 'rb') as f:
    edegem_geojson = json.loads(f.read())


heritage_objects = requests.post(
    'https://geo.onroerenderfgoed.be/zoekdiensten/afbakeningen',
    json={
        "categorie": ["erfgoedobjecten", "aanduidingsobjecten"],
        "geometrie": edegem_geojson
    },
    headers={"Content-type": "application/json", "Accept": "application/json"}
).json()

municipality_body = {
    "params": {
        "width": 1000,
        "height": 1000
    },
    "layers": [
        {
            "type": "text",
            "text": "© GRB basiskaart, informatie Vlaanderen",
            "gravity": "south_east",
            "font_size": 4
        },
        {
            "type": "wms",
            "url": "http://geoservices.informatievlaanderen.be/raadpleegdiensten/GRB-basiskaart-grijs/wms?",
            "layers": "GRB_BSK_GRIJS"
        }
    ]
}

# Make a map of the municipality to show all the heritage objects

for obj in heritage_objects:
    municipality_body['layers'].append(
        {
            "type": "geojson",
            "geojson": obj["geometrie"]
        }
    )

with open(os.path.join(os.path.dirname(__file__), 'maps/Edegem/Edegem.png'), 'wb') as f:
    f.write(Generator.generate_stream(municipality_body))
