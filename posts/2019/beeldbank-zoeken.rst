.. post:: 
   :category: services, imagebase
   :tags: beeldbank, search, full-text
   :author: Koen Van Daele
   :language: nl

Zoeken in de beeldbank
======================

We hebben het de laatste tijd al vaak gehad over de nieuwe inventaris
(:ref:`inventaris-nieuw`), maar we hebben in 2019 ook een nieuwe `beeldbank
<https://beeldbank.onroerenderfgoed.be>`_ gelanceerd. Deze vervangt zowel een 
oude module die inherent was aan de inventaris als de beeldbank die ooit voor 
het VIOE ontwikkeld werd. De nieuwe beeldbank bevat ondertussen zo'n 277.000 
afbeeldingen, waarvan een grote meerderheid vrij mag hergebruikt worden zolang 
de `gebruiksvoorwaarden gevolgd worden <https://beeldbank.onroerenderfgoed.be/hergebruik>`_.
Vandaag geven we je wat meer uitleg bij de zoekfuncties van de beeldbank en hoe
je er het meeste uit kan halen.

Als je naar de `homepagina van de beeldbank
<https://beeldbank.onroerenderfgoed.be>`_ surft, dan zie je daar bovenaan een
simpele zoekbalk. Deze helpt je om als een typische zoekmachine op basis van
één of meerdere termen te zoeken. Je tikt er de termen in die je relevant acht
en de toepassing doet zijn werk. Stel dat ik op zoek ben naar afbeeldingen over
de Knokkestraat, dan tik ik `Knokkestraat` in en druk op *zoeken*. We krijgen
18 resultaten, gesorteerd volgens relevantie. Net zoals bij de inventaris
(:ref:`inventaris-zoeken-full-text`) geeft de beeldbank ons de afbeeldingen
gesorteerd volgens de mate waarin ze voldoen aan de zoekvraag. Het meest
`knokkestraat`-achtige object staat vooraan. Dit zijn een aantal afbeeldingen
van huizen in de Knokkestraat te Knokke-Heist, waarbij Knokkestraat zowel in de
titel van de afbeelding als bij het adres staat. Daarna volgen afbeeldingen uit
de Knokkestraat in Diksmuide, Zwevegem en tenslotte Wachtebeke. Bij die laatste
is Knokkestraat wel aanwezig in de titel van het object, maar niet in het
adres.

Op deze zoekpagina kunnen we het zoekresultaat ook verfijnen. Daarvoor
gebruiken we zogenaamde facetten. Dit zijn filters die we kunnen instellen op
de bestaande dataset. In dit geval kunnen we expliciet filteren op `Provincie`,
`Gemeente`, `Jaar`, `Maker` en `Licentie`. Bij elk facet zie je alle mogelijke
waarden, inclusief hoe vaak ze voorkomen. Zo zien we dat er 8 afbeeldingen uit
Knokke-Heist zijn en maar 1 uit Diksmuide. Het laatste facet, licentie, geeft
aan onder welke voorwaarden een afbeeling hergebruikt kan worden. Zo zien we
dat 17 afbeeldingen vrij voor hergebruik zijn onder één van twee licenties en
dat 1 afbeelding niet vrijgegeven is voor hergebruik.

De facetten spreken redelijk hard voor zich, het tekstveld vrij zoeken kan nog
wel wat uiteg gebruiken. Net zoals bij de inventaris kan je hier full-text
zoeken operatoren op toepassen:

* Als je meerdere zoektermen opgeeft, dan combineer je die impliciet als EN.
  Dus, als je zoekt naar `molen knokke`, dan vraag je naar alle afbeeldingen
  waarin zowel de term `molen` als de term `knokke` voorkomt. Je kunt dit ook
  expliciet maken met de `&` operator. Dus, `molen knokke` en `molen & knokke`
  zijn exact hetzelfde.
* Als je wil zoeken naar afbeeldingen waarin ofwel `molen` ofwel `knokke`
  voorkomen, dan gebruik je de `|` operator. Dus, `molen | knokke`. Dat zijn er
  natuurlijk heel wat meer.
* Stel dat je een bepaalde zoekterm niet wenst te vinden, dan gebruik je de `-`
  operator. Deze plaats je vlak voor de zoekterm die je niet wenst te zien.
  Dus, `molen -knokke` om alle molens waar Knokke niet in voorkomt te zien.
* Indien je meerdere zoektermen als één zoektermen wenst te beschouwen, plaats
  je die tussen aanhalingstekens. Stel dat ik zoek naar `van daele`, dan krijg
  ik 7 afbeeldingen waarin zowel het woord `van` als het woord `daele`
  voorkomt. Stel dat ik echter afbeeldingen zoek van een fotograaf `van daele`,
  dan kan ik zoeken naar `"van daele"` om alles van deze fotograaf te zien.
* Indien ik slechts op een deel van een woord wil zoeken, dan kan ik de
  wildcard `*` gebruiken. Let op, dit werkt enkel op het einde van een woord.
  Als ik bv. zoek naar `dorp*`, dan krijg ik afbeeldingen waarin zowel
  `dorpstraat`, `dorpswoning` als `dorp` voorkomen.
* Tenslotte kan je haakjes `()` gebruiken om zoekoperatoren te groeperen. Zo kan
  je met `dorp* (knokke-heist | brugge)` zoeken naar afbeeldingen waarin termen
  voorkomen die beginnen met `dorp` en waarin ofwel `knokke-heist` ofwel
  `brugge` voorkomen.

Denk er aan, als je met het algemene zoekveld zoekt, zoek je bepaale termen.
Als dus zoekt naar `brugge*`, kan je zowel afbeeldingen vinden die iets te
maken hebben met `bruggen`, als afbeeldingen uit de gemeente `brugge`.

Je kunt dergelijke zoekopdrachten perfect combineren met de facetten. Dus als
je zoekt naar `brugge*` en daarna kruis je het jaar `2019` aan, dan zie je alle
afbeeldingen uit 2019 waarin een woord voorkomt dat start met `brugge`.
