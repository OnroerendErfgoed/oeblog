.. post:: 2017-08-14
   :category: services, GIS
   :tags: geozoekdiensten
   :author: Koen Van Daele
   :language: nl

Geozoekdiensten. Wat ligt er hier?
==================================

Zoals beloofd (:ref:`waar-ligt-ons-erfgoed`) geven we je graag wat meer informatie over onze
Geozoekdiensten. Deze zoekdiensten bestaan momenteel uit één enkele webservice
die uitermate geschikt is om één enkele vraag te beantwoorden: `Wat ligt er in
een bepaald gebied?` De gebruiker of client stuurt een geometrie naar de
webservice en de webservice laat weten welk erfgoed er deels of geheel in deze
geometrie ligt. Dit resultaat is een simpele `JSON` datastructuur waarin je
voor elk object informatie krijgt zoals een `id`, een `uri`, een `type` en de
volledige `geometrie`.

Zoals vaak zegt een voorbeeld meer dan duizend woorden. Stel dat we al het
erfgoed willen kennen in een straal van honderd meter rond een bepaald punt in
Vlaanderen:

.. code-block:: bash

    $ curl -X GET --header 'Accept: application/json' 'https://geo.onroerenderfgoed.be/zoekdiensten/afbakeningen?categorie=aanduidingsobjecten&geometrie=%7B%22type%22%3A%20%22Point%22%2C%20%22coordinates%22%3A%20%5B4.7676665601685%2C50.985228897907%5D%7D&buffer=100'

Daarop krijgen we een lijst van resultaten terug. Elke van deze resultaten is
een `JSON` object met de attributen `id`, `uri`, `categorie`, `type`, `naam` en
`geometrie`.

.. literalinclude:: erfgoedobject_detail.json
    :language: json

Het attribuut `naam` geeft een korte beschrijving van het object. Het `id`
identificeert het object uniek binnen de dataset waar het uit komt. De `uri`
identificeert het object eveneens uniek, maar is gegarandeerd uniek over alle
datasets heen. Je kunt dit zien als een globale, unieke identificator. En wat
meer is, de `uri` is eigenlijk gewoon een link die je naar meer informatie zal
leiden. Indien je dus https://inventaris.onroerenderfgoed.be/erfgoedobjecten/134454
opvraagt via de browser kom je uit op een pagina over het object in de
`Inventaris Onroerend Erfgoed <https://inventaris.onroerenderfgoed.be>`_. Indien
je liever de achterliggende ruwe data in `JSON` formaat bekijkt, dan stuur je
een `Accept: application/json` header mee in een GET request.

.. code-block:: bash

    $ curl -L -X GET --header 'Accept: application/json' 'https://id.erfgoed.net/erfgoedobjecten/134454'

In dit geval hebben we een erfgoedobject gevonden uit de wetenschappelijke
inventaris van tuinen en parken. Dit kunnen we afleiden uit het attribuut
`type`. Dit is een object met een `uri` en een `label`. De uri verwijst telkens
naar een term in een thesaurus van `inventaristypes` of `aanduidingstypes`. Als
je meer wenst te weten over dit type, volg je de `uri` naar de de achterliggende
thesaurus. Daar kun je bijvoorbeeld te weten komen dat deze inventaris soms ook
met de code `ile_park` benoemd wordt.

De geometrie wordt in `geojson` formaat doorgestuurd. Omdat de geografische
informatie nogal groot kan zijn en mogelijk ook niet zo relevant, kun je de
service ook laten weten dat je deze niet wenst te ontvangen:

.. code-block:: bash

    $ curl -X GET https://geo.onroerenderfgoed.be/zoekdiensten/afbakeningen?&buffer=100&geef_geometrie=0

Standaard zal de service naar alle soorten objecten zoeken, maar je kan hier ook
in filteren met de parameter `categorie`. Hierin heb je verschillende
mogelijkheden:

- **Erfgoedobjecten**: Deze categorie bevat alle inhoudelijke objecten die met
  erfgoed te maken hebben. Dit zijn de `wetenschappelijke inventarissen`.
- **Aanduidingsobjecten**: De aanduidingsobjecten of aanduidingen zijn de juridische
  verankeringen van erfgoedobjecten. Deze kunnen zowel `beschermd` als `vastgesteld`
  zijn (wat je dan weer kunt afleiden uit de URI's van de types). Verder vallen
  hier ook nog de `erfgoedlandschappen` en de `Unesco kernzones` en `Unesco
  bufferzones` onder.
- **Plannen**: Deze categorie bevat nu enkel de `beheersplannen` en zal op termijn
  uitgebreid worden met de `erfgoedrichtplannen`

Stel dat je enkel de objecten wenst te zien die aangeduid zijn:

.. code-block:: bash

    $ curl -X GET https://geo.onroerenderfgoed.be/zoekdiensten/afbakeningen?&buffer=100&geef_geometrie=0&categorie=aanduidingsobjecten

In dat geval krijg je dus enkel beschermingen, vaststellingen of
erfgoedlandschappen te zien.

Voor simpele vragen zoals `Geef me al het erfgoed in een straal rond een punt`
werkt de bovenstaande request prima. Je hoeft je echter niet te beperken tot
punten, maar kunt ook (multi-)polygonen en lijnen gebruiken. Op dat moment wordt
het echter al snel heel onhandig om de GeoJSON voorstelling van de geometrie
waarmee je zoekt in de URL op te nemen. Daarom dat je ook met een `POST` request
kunt werken waarbij je de vraag die je stelt kunt opnemen in de body van de
request.

Ben je benieuwd naar deze nieuwe service en wil je er mee aan de slag, dan kan
dat. De service is vrij toegankelijk voor iedereen en we kunnen het hergebruik
alleen maar aanmoedigen. Om makkelijk te zien wat de service kan, raden we
onze levende api documentatie aan. Deze kan je raadplegen op
https://geo.onroerenderfgoed/zoekdiensten/api_doc

De geozoekdiensten zijn een vrij simpele webservice die heel veel informatie kan
bieden. We hopen dan ook dat deze voor de buitenwereld even nuttig zal zijn als
voor ons. We vernemen graag wat jullie er van vinden en of jullie nog
bijkomende noden hebben. Opmerkingen, vragen of verdere wensen mag je ons toesturen
via mailto:ict@onroerenderfgoed.be.
