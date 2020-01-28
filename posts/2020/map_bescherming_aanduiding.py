# -*- coding: utf-8 -*-
"""
Dit script aanvaardt een csv bestand met naamgeving oude_beschermingsnummers.csv en genereert een nieuw CSV bestand
met een mapping van de oude beschermingsnummers en hun nieuwe URI

Stel dat het oude beschermingsnummer beschikbaar was via
https://inventaris.onroerenderfgoed.be/erfgoed/beschermd/OW000521, dan zal het script een zoekopdracht starten op dit
nummer via https://inventaris.onroerenderfgoed.be/aanduidingsobjecten?ander_nummer=OW000521.
De resultaten van die zoekopdracht zijn de URI's van de beschermingen gekoppeld aan het oud beschermingsnummer.

Gebruik: python map_bescherming_aanduiding.py
Het input CSV bestand dient in dezelfde map te staan als het python script
Een output CSV wordt aangemaakt, eveneens in dezelfde map als het script

Het input bestand oude_beschermingsnummers.csv is een lijst met 1 beschermingsnummer per regel. Bijvoorbeeld:
OW000521
OW000522
OW000523
OW000524
OW000525

Output bestand krijgt de naamgeving mapping_beschermingsnummer_aanduidingsuri.csv.
Dit is een ; gescheiden CSV met per rij:
- Het oude beschermingsnummer
- een met komma gescheiden opsomming van URI's die gekoppeld zijn aan het oude beschermingsnummer.
Voorbeeld:
OW000525;https://id.erfgoed.net/aanduidingsobjecten/11982
OW000524;https://id.erfgoed.net/aanduidingsobjecten/12062
OW000521;https://id.erfgoed.net/aanduidingsobjecten/11965
OW000523;https://id.erfgoed.net/aanduidingsobjecten/12217,https://id.erfgoed.net/aanduidingsobjecten/1
OW000522;https://id.erfgoed.net/aanduidingsobjecten/11961,https://id.erfgoed.net/aanduidingsobjecten/2
"""
import requests
import csv
from requests.exceptions import HTTPError

mapping = dict()
oude_beschermingsnummers = list()
url_template = 'https://inventaris.onroerenderfgoed.be/aanduidingsobjecten?ander_nummer={oud_beschermingsnummer}'
bronbestand = 'oude_beschermingsnummers.csv'
headers = {'accept': 'application/json'}

with open(bronbestand, 'rb') as csv_bestand:
    reader = csv.reader(csv_bestand)
    for row in reader:
        oude_beschermingsnummers.append(row[0])

for oud_id in oude_beschermingsnummers:
    mapping[oud_id] = list()
    url = url_template.format(oud_beschermingsnummer=oud_id)
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        for item in r.json():
            mapping[oud_id].append(item['uri'])
    except HTTPError as http_err:
        mapping[oud_id].append('HTTP fout bij het ophalen van het beschermingsnummer: {msg}'.format(msg=http_err))
    except Exception as err:
        mapping[oud_id].append('Onverwachte fout bij het ophalen van het beschermingsnummer: {msg}'.format(msg=err))

with open('mapping_beschermingsnummer_aanduidingsuri.csv', 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=';')
    for key, value in mapping.items():
        row = [key] + [','.join(value)]
        writer.writerow(row)
