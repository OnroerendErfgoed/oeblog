.. post::
   :tags: GIS
   :category: services
   :author: Koen Van Daele
   :language: nl

Geozoekdiensten. Wat ligt er hier?
==================================

Zoals beloofd (:ref:`waar-ligt-ons-erfgoed`) geven we je graag wat meer informatie over onze
Geozoekdiensten. Deze zoekdiensten bestaan momenteel uit één enkele webservice 
die uitermate geschikt is om één enkele vraag te beantwoorden: `Wat ligt er in 
een bepaald gebied?`. De gebruiker of client stuurt een geometrie naar de 
webservice en de webservice laat weten welk erfgoed er deels of geheel in deze 
geometrie ligt. Dit resultaat is een simpele `JSON` datastructuur waarin je 
voor elk object informatie krijgt zoals een `id`, een `uri`, een `type` en de 
volledige `geometrie`.
