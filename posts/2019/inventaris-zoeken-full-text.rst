.. post::
   :category: services
   :tags: inventaris
   :author: Koen Van Daele
   :language: nl

Full text zoeken in de inventaris
=================================

Sinds `13 mei <https://www.onroerenderfgoed.be/nieuws/inventaris-onroerend-erfgoed-vernieuwd>`_
staat er een gloednieuwe inventaris op https://inventaris.onroerenderfgoed.be.
Zoals altijd is het even aanpassen. Omdat verandering altijd even wennen is, lijsten we
op onze IT blog de voornaamste mogelijkheden qua zoeken op. De vorige keer 
(:ref:`inventaris-zoeken-inleiding`) gaven we een aantal algemene principes mee,
vandaag verdiepen we ons in full-text zoeken. 

.. warning::
   Omdat de nieuwe inventaris nog vers is, kunnen er nog lichte 
   verschuivingen optreden, dus mogelijk is nog niet alles definitief.

Zoals we in ons vorige bericht al uitlegden, komt full-text zoeken overeen met 
zoeken zoals een grote zoekmachine op het internet. Onze zoekmachine gaat er 
van uit dat je op zoek bent naar een vrij specifiek object of document en 
probeert je het best passende terug te geven. De zoekmachine doet dit door je
zoektermen te bekijken, alle objecten te zoeken die aan je zoektermen voldoen 
en tenslotte de meest relevante objecten vooraan te zetten. Als je naar 
`Gravensteen` zoekt, krijg je dus het meest `Gravensteenige` object te zien.

Om te bepalen wat nu het meest relevante object is, zijn er meerdere algoritmes
die kunnen gebruikt worden. In grote lijnen komt het echter op neer dat een
object waarin je zoekterm meer voorkomt, als meer relevant wordt gezien dan een
object waarin je zoekterm minder voorkomt. Hierbij wordt er rekening gehouden
met andere factoren zoals de lengte van het veld waarin een zoekterm voorkomt
(hoe kleiner een veld, hoe relevanter de zoekterm) en hoe vaak je zoekterm
voorkomt over alle objecten heen (hoe vaker, hoe minder relevant de zoekterm).
Daarnaast hebben we de zoekmachine ook zo geconfigureerd dat het voorkomen van 
een zoekterm in bepaalde velden meer relevant is dan in andere. Zo gaan we er 
van uit dat de titel meer doorweegt dan de tekst van een fiche. Als je naar 
`Gravensteen` zoekt, zal een object met als titel `Gravensteen` hoger scoren
dan een object waarin `Gravensteen` een keer in de tekst voorkomt.

Als we even naar de zoekmachine kijken, dan kunnen we simpelweg zoeken naar het
`Gravensteen` door op
https://inventaris.onroerenderfgoed.be/erfgoedobjecten/zoeken in het veld
`Algemeen` de zoekterm `Gravensteen` in te tikken. Dit geeft ons
https://inventaris.onroerenderfgoed.be/erfgoedobjecten?tekst=gravensteen als
resultaat en het Gravensteen uit Gent staat bovenaan. Niet geheel onverwacht.
Het maakt trouwens ook helemaal niet uit of we zoeken op `Gravensteen` of
`gravensteen`.

Stel echter dat we iets meer willen weten over het Gravensteen in Aalst. Als we
`Gravensteen Aalst` als zoekterm gebruiken, dan krijgen we nog maar 2
resultaten. Dit zijn dus allemaal objecten waarin zowel `Gravensteen` als
`Aalst` voorkomen. Standaard wordt elk woord in het zoekvenster dus gezien als
een zoekterm en wordt er gezocht naar objecten waarin alle termen voorkomen. We
kunnen dit expliciet maken met de AND operator. Deze stellen we voor met een `+` 
teken. Dus `Gravensteen Aalst` is identiek aan `Gravensteen+Aalst`. Stel dat we
echter op zoek zijn naar iets over het `Gravensteen` of `Aalst`, dan kunnen we
de OR operator gebruiken. Deze stellen we voor met een `|` teken, ook gekend
als het pipe symbool. Dus `Gravensteen|Aalst` geeft ons alles waarin zowel
`Gravensteen` als `Aalst` voorkomen. De derde operator is de NOT operator. Deze
stellen we voor met een `-` teken. Dus, als we alle objecten willen waarin
`Gravensteen` voorkomt, maar niet `Aalst`, dan zoeken we `Gravensteen -Aalst`.

Soms willen we echter niet dat een spatie als een aparte zoekterm gezien wordt.
Stel dat we willen zoeken naar de Grote Markt te Aalst. Als we zoeken naar
`Grote Markt Aalst`, dan krijgen we vrij veel zoekresultaten. Bovenaan staat
inderdaad de Grote Markt, maar we vinden helemaal achteraan wel 
https://inventaris.onroerenderfgoed.be/erfgoedobjecten/1996, waarin de woorden
`grote`, `markt` en `aalst` voorkomen. Als we expliciet willen zoeken naar de
Grote Markt, dan kunnen we deze tussen aanhalingstekens plaatsen. Dus, met
`"Grote Markt" Aalst` zoeken we niet meer naar drie zoektermen, maar naar twee
zoektermen. Zowel `Grote Markt` als `Aalst` moeten voorkomen. We krijgen al wat
minder zoekresultaten en een object zoals het paviljoen van de Notelaer valt
al weg.

Eens we met meerdere zoektermen beginnen te werken, willen we misschien wel
complexere combinaties van zoektermen toepassen ook. Stel dat we interesse
hebben in de Vismarkt van Brugge of Gent. Als we zoeken naar `vismarkt brugge
gent`, dan zoeken we objecten waarin alle drie die termen voorkomen. Niet echt
wat we zochten, want die van Brugge maakt geen melding van die van Gent en die
van Gent niet van Brugge. Dus we krijgen geen van de door ons gewenste
vismarkten. We kunnen proberen met `vismarkt + brugge | gent`. Nu
krijgen we heel veel resultaten omdat we eigenlijk gezocht hebben op objecten over
de vismarkt in Brugge, of objecten in Gent. Geen nodd, we kunnen wel zoektermen
groeperen door haakjes `()` te gebruiken. Zo kunnen we zoeken naar `vismarkt +
(brugge|gent)` om fiches te vinden over de `vismarkt` waarin ook nog `Brugge`
of `Gent` voorkomen.

Tenslotte kunnen we soms ook wel eens willen zoeken op een deel van een woord.
Stel dat we iets zoeken over gedenkstenen, gedenkplaten of gelijkaardig, dan
kunnen we zoeken aanr `gedenk*`. Dit kan prima gecombineerd worden met de
vorige operatoren, dus met `gedenk* | herdenk*` komen we allerlei te weten over
herdenkingsbomen, gedenkstenen, gedenkplaten, herdenkingsmonumenten en meer.
Denk er wel aan dat het `*` teken enkel op het einde van een zoekterm kan gebruikt
worden omwille van de performantie van zoekopdrachten. Met `*linde` zal je dus
geen herdenkingslinde vinden.

Als we alles combineren kunnen we dus zoeken naar objecten waarin iets gezegd
wordt over visgraatverband of -motief, in Oost- of West-Vlaanderen, maar waarin
Brugge niet voorkomt met de volgende zoekopdracht: `visgraat*
(oost-vlaanderen|west-vlaanderen) -brugge`.

Misschien vraag je je af welke velden er nu juist doorzocht worden als je
full-text zoekt en hoe zwaar deze doorwegen in je zoekopdracht? In het 
bovenstaande voorbeeld zul je bijvoorbeeld objecten vinden waarin
Oost-Vlaanderen of West-Vlaanderen niet in de tekst voorkomen. Omdat het echter
makkelijker werkt en aangeeft waar de nodige accenten liggen, voegen we deze
toch toe aan de full-text index. De velden die we full-text doorzoeken in
volgorde van belang zijn: de tekst, de titel van de tekst, de korte
beschrijving van het object (wat je te zien krijgt in een zoekresultaat),
provincie, gemeente, deelgemeente en straat namen, thesaurustermen en de naam
van het object zelf. Als je dus `vismarkt` zoekt, dan zal een object waarvan de
titel `vismarkt` is, hoger op de lijst staan dan een object waarvan `vismarkt`
ergens in de tekst voorkomt.

We hopen dat het duidelijk is dat je met de nieuwe zoekmachine in de inventaris
krachtige full-text zoekopdrachten kunt uitvoeren eens je de mogelijkheden een
beetje onder de knie hebt. Samengevat zijn die:

* Meerdere zoektermen worden impliciet met AND gecombineerd, je kan dit
  expliciet maken met `+`
* Je kunt ze ook combineren met een OR combinatie via `|`
* Je kunt een term uitsluiten met de NOT operator via `-`
* Je kunt zoektermen combineren tot 1 zoekterm door de termen tussen `"` te
  plaatsen
* Je kunt de volgorde van operatoren aanpassen door `()` te gebruiken
* Je kunt zoeken op woorden die starten met een prefix door een `*` toe te
  voegen 
