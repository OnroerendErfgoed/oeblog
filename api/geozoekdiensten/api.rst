====================
Service Documentatie
====================

.. http:get:: /afbakeningen

    Simpele zoekactie naar afbakeningen van objecten, dossiers of plannen.

    Dit endpoint stelt ons in staat om te vragen naar resources die op een
    bepaalde plaats aanwezig zijn. De resources worden onderverdeeld in 3 grote
    categorieën:

    * **erfgoedobjecten:** Erfgoedobjecten uit de wetenschappelijke inventaris.
    * **aanduidingsobjecten:** Dit zijn de afbakeningen met rechtsgevolgen, het
      gaat om beschermingen en vastgestelde inventarissen.
    * **plannen:** Beheersplannen uit authentieke bron beheersplannen. Kan op
      termijn worden uitgebreid met erfgoedrichtplannen.
    * **dossiers:** Advies-, premie- en andere dossiers uit de authentieke
      bron dossiers.

    .. deprecated:: 0.2.0
       In versie `0.1.0` was er een categorie `objecten`. Deze is deprecated en
       zal verwijderd worden in versie `0.4.0`. Voorlopig werkt deze nog.
       Eenzelfde gedrag als vroeger kan bekomen worden met
       `?categorie=erfgoedobjecten&categorie=aanduidingsobjecten`.


    **Example Request**:

    .. sourcecode:: http

        GET /afbakeningen HTTP/1.1
        Host: localhost
        Accept: application/json
        Range: items=0-19


    **Example Request**:

    .. sourcecode:: http

        GET /afbakeningen?categorie=aanduidingsobjecten HTTP/1.1
        Host: localhost
        Accept: application/json
        Range: items=0-19


    **Example Request**:

    .. sourcecode:: http

        GET /afbakeningen?categorie=aanduidingsobjecten&geometrie={"type":"Point","coordinates":[4.430750, 51.149166]}&buffer=1000 HTTP/1.1
        Host: localhost
        Accept: application/json
        Range: items=0-19


    :query categorie: Enkel de afbakeningen van resources uit een bepaalde categorie doorzoeken.
            Toegestane waarden op dit moment zijn: `erfgoedobjecten`, `aanduidingsobjecten`, `dossiers` en `plannen`.
            De oude categorie `objecten` is deprecated.
    :query geometrie: (verplicht) Een GeoJSON geometry waarmee gezocht wordt. Deze parameter is verplicht.
        Een GeometryCollection kan niet gebruikt worden om mee te zoeken.
        De geometry mag niet groter zijn dan 80 km² en moet binnen Vlaanderen 
        liggen (De grens van Vlaanderen is hiervoor gebufferd met 1km en versimpeld met tolerantie 500m)
        De geometry kan een eigen crs opgeven zoals normaal bij GeoJSON. Indien afwezig,
        vallen we terug op de GeoJSON specs: WGS84 (EPSG:4326).
    :query buffer: Een getal dat een buffer (uitgedrukt in m) voorstelt rond een
        geometrie waarmee gezocht wordt. Enkel relevant indien er ook een 
        geometrie wordt opgegeven. Dit getal moet tussen 0 en 5000 liggen. De 
        geometrie gecombineerd met een buffer mogen niet groter zijn dan 80 km²
    :query geef_geometrie: Boolean `0` of `1`. Standaard `1`.
        Geeft aan of de service ook de geometry van de gevonden afbakeningen
        moet terugsturen.
    :reqheader Range: Kan gebruikt worden om een zekere set van resultaten weer te geven,
        bv. ``items=0-24`` zal de eerste 25 resultaten opvragen.

    **Example Response**:

    .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json
      Content-Range: items 0-1/286

      [
        {
            "categorie": "erfgoedobjecten",
            "naam": "Naam ergoedobject",
            "uri": "https://id.erfgoed.net/erfgoedobjecten/1",
            "id": "1",
            "type": "https://id.erfgoed.net/thesauri/inventaristypes/6",
            "geometrie": {
                "type": "MultiPolygon",
                "coordinates": [
                    [
                        [[30, 20], [45, 40], [10, 40], [30, 20]]
                    ], [
                        [[15, 5], [40, 10], [10, 20], [5, 10], [15, 5]]
                    ]
                ],
                "crs": {
                    "type": "name",
                    "properties": {
                        "name": "EPSG:31370"
                    }
                }
            }
        }, {
            "categorie": "aanduidingsobjecten",
            "naam": "Naam ergoedobject2",
            "uri": "https://id.erfgoed.net/aanduidingsobjecten/2",
            "id": "2",
            "type": "https://id.erfgoed.net/thesauri/aanduidingstypes/2",
            "geometrie": {
                "type": "MultiPolygon",
                "coordinates": [
                    [
                        [[30, 20], [45, 40], [10, 40], [30, 20]]
                    ], [
                        [[15, 5], [40, 10], [10, 20], [5, 10], [15, 5]]
                    ]
                ],
                "crs": {
                    "type": "name",
                    "properties": {
                        "name": "EPSG:31370"
                    }
                }
            }
        }
      ]


    :resheader Content-Range: Laat de gebruiker weten wat de reikwijdte is van de resultaten die worden teruggegeven,
            bv. ``items=0-24/306`` voor de eerste 25 resultaten uit een totaal van 306.
    :statuscode 200: Afbakeningen werden gevonden.
    :statuscode 400: De zoekacties kan niet worden uitgevoerd wegens problemen
        met de zoekparameters.


.. http:post:: /afbakeningen


    Een alternatieve manier om afbakeningen te zoeken. Met een
    :http:method:`post` kan de query gesteld worden door ze als JSON file op te
    nemen in de body van de request.

    .. sourcecode:: http

        POST /afbakeningen
        Host: localhost
        Accept: application/json
        Range: items=0-19

        {
            "categorie": "erfgoedobjecten",
            "uri": "https://id.erfgoed.net/erfgoedobjecten/156",
            "id": "156",
            "type": "https://id.erfgoed.net/thesauri/inventaristypes/8",
            "geometrie": {
                "type": "MultiPolygon",
                "coordinates": [
                    [[[131078.11588438248,191894.5202434389],
                    [132292.5722846411,191409.89857776184],
                    [132111.37356717332,191242.3774296688],
                    [130787.15852207821,191355.16772503313],
                    [131078.11588438248,191894.5202434389]]]
                ],
                "crs": {
                    "type": "name",
                    "properties": {
                        "name":"urn:ogc:def:crs:EPSG::31370"
                    }
                }
            }
        }

.. http:get:: /administratievegrenzen

    Zoek naar de administratieve grenzen van iets. Deze service gaat in
    verschillende databestanden kijken en zoekt binnen welke grenzen een query
    valt.

    De volgende lagen worden doorzocht:

     * gewesten
     * provincies
     * arrondissementen
     * gemeenten

    :query geometrie: (optioneel) Een GeoJSON geometry waarmee gezocht wordt. Deze parameter is verplicht.
        Een GeometryCollection kan niet gebruikt worden om mee te zoeken.
        De geometry mag niet groter zijn dan 80 km² en moet binnen Vlaanderen liggen (De grens van Vlaanderen is hiervoor gebufferd met 1km en versimpeld met tolerantie 500m)
        De geometry kan een eigen crs opgeven zoals normaal bij GeoJSON. Indien afwezig,
        vallen we terug op de GeoJSON specs: WGS84 (EPSG:4326).
    :query buffer: Een getal dat een buffer (uitgedrukt in m) voorstelt rond een
        geometrie waarmee gezocht wordt. Enkel relevant indien er ook een
        geometrie wordt opgegeven.
        Dit getal moet tussen 0 en 5000 liggen. De geometrie gecombineerd
        met een buffer mogen niet groter zijn dan 80 km²
    :query type: (optioneel) Eén of meerdere van de volgende opties:
        * gewest
        * arrondissement
        * provincie
        * gemeente
        Indien deze parameter niet aanwezig is, worden alle grenzen doorzocht.

    **Example Request**:

    .. sourcecode:: http

        Vraag alle gekende administratieve grenzen op.

        GET /administratievegrenzen HTTP/1.1
        Host: localhost
        Accept: application/json
        Range: items=0-1

    **Example Request**:

    .. sourcecode:: http

        Vraag de gekende administratieve grenzen van het type gemeente of
        provincie op.

        GET /administratievegrenzen?type=gemeente&type=provincie HTTP/1.1
        Host: localhost
        Accept: application/json
        Range: items=0-1

    **Example Response**:

    .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json
      Content-Range: items 0-1/231

      [
        {
            "naam": "Gent",
            "id": "44021",
            "type": "gemeente",
            "geometrie": {
                "type": "MultiPolygon",
                "coordinates": [
                    [
                        [[30, 20], [45, 40], [10, 40], [30, 20]]
                    ], [
                        [[15, 5], [40, 10], [10, 20], [5, 10], [15, 5]]
                    ]
                ],
                "crs": {
                    "type": "name",
                    "properties": {
                        "name": "EPSG:31370"
                    }
                }
            }
        }, {
            "naam": "Oost-Vlaanderen",
            "id": "40000",
            "type": "provincie",
            "geometrie": {
                "type": "MultiPolygon",
                "coordinates": [
                    [
                        [[30, 20], [45, 40], [10, 40], [30, 20]]
                    ], [
                        [[15, 5], [40, 10], [10, 20], [5, 10], [15, 5]]
                    ]
                ],
                "crs": {
                    "type": "name",
                    "properties": {
                        "name": "EPSG:31370"
                    }
                }
            }
        }
      ]


.. http:post:: /administratievegrenzen

    Een alternatieve manier om administratieve grenzen te zoeken. Met een
    :http:method:`post` kan de query gesteld worden door ze als JSON file op te
    nemen in de body van de request.

    .. sourcecode:: http

        POST /administratievegrenzen
        Host: localhost
        Accept: application/json
        Range: items=0-1

        {
            "naam": "Oost-Vlaanderen",
            "id": "40000",
            "type": "provincie",
            "geometrie": {
                "coordinates": [
                    [[[131078.11588438248,191894.5202434389],
                    [132292.5722846411,191409.89857776184],
                    [132111.37356717332,191242.3774296688],
                    [130787.15852207821,191355.16772503313],
                    [131078.11588438248,191894.5202434389]]]
                ],
                "crs": {
                    "type": "name",
                    "properties": {
                        "name":"urn:ogc:def:crs:EPSG::31370"
                    }
                }
            }
        }
    
