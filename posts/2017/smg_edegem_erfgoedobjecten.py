# -*- coding: utf-8 -*-
import os
import json
import requests
from copy import deepcopy
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

# Make a map of each heritage object in the municipality
# As an example only show the first

body = {
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
            "url": "http://geoservices.informatievlaanderen.be/raadpleegdiensten/omwrgbmrvl/wms?",
            "layers": "Ortho"
        }
    ]
}

for obj in heritage_objects:
    if "Polygon" in obj["geometrie"]["type"]:
        obj_body = deepcopy(body)
        obj_body['layers'].append(
            {
                "type": "geojson",
                "geojson": obj["geometrie"]
            }
        )
        obj_body['layers'].append(
            {
                "type": "text",
                "text": obj["naam"],
                "gravity": "north_west",
                "font_size": 6
            }
        )

        filename = obj["naam"].replace(" ", "_").strip() + '.png'
        with open(os.path.join(os.path.dirname(__file__), 'maps/Edegem', filename), 'wb') as f:
            f.write(Generator.generate_stream(obj_body))
