.. post:: 2019-08-14
   :category: inventory
   :tags: inventaris
   :author: Koen Van Daele
   :language: nl

Tien jaar inventaris
====================

Sinds `13 mei <https://www.onroerenderfgoed.be/nieuws/inventaris-onroerend-erfgoed-vernieuwd>`_
staat er een gloednieuwe inventaris op https://inventaris.onroerenderfgoed.be.
Op het eerste zicht ziet ze er vooral heel erg anders uit, maar wie de vorige
inventaris goed kende herkent heel veel zaken. De gegevens op de
inventariswebsite zijn namelijk nog altijd dezelfde als vroeger: het erfgoed
waar Vlaanderen rijk aan is. Net zoals vroeger kan je er zowel lezen wat dat
erfgoed dan wel is en wat de rechtsgevolgen zijn die vasthangen aan een
bepaalde stukje erfgoed. Achter de schermen is er echter heel wat veranderd en
werd de onderliggende technologie volledig herschreven. Het lijkt misschien of
de inventaris tien jaar ongewijzigd is gebleven en dan in zijn geheel vervangen
werd. Niets is echter minder waar, in de loop van die tien jaar zijn er heel
wat wijzigingen geweest. Vandaag gaan we even dieper in op de evoluties die onze
inventaris de laatste 10 jaar meegemaakt heeft, met een sterke focus op de
technologische kant.

Wat toen nieuw was, is nu oud
-----------------------------

De nieuwe inventaris volgt de nieuwe technologische principes en de algemene
architectuur die het agentschap Onroerend Erfgoed hanteert sinds 2014. Na de
samensmelting van het `Vlaams Instituut voor het Onroerend Erfgoed` (VIOE) en het
agentschap `Ruimte en Erfgoed`, beschikte het agentschap over een zeer divers
technologisch landschap. Al vrij snel werd er beslist over te gaan tot een
nieuwe `technology stack`.

Er was al lang een sterke voorkeur aanwezig voor
`open source software` bij het VIOE en die keuze werd behouden. Qua
systeembeheer leidde dit tot een verderzetting van het werken met \*nix
servers, met name Debian of Ubuntu servers. Op het gebied van databanken was 
er al lang een voorkeur voor de `PostgreSQL databank server <https://www.postgresql.org>`_.
Er was geen enkele reden om hiervan af te wijken. Deze technologie deed wat ze 
moest doen, kon perfect de volumes aan die we moesten kunnen verwerken en kende 
geen licentiekost. Daarnaast beschikte ze met de `Postgis <https://postgis.net>`_ 
plugin over een extreem krachtige GIS motor, onontbeerlijk voor een agentschap 
dat dagelijk met onroerend erfgoed bezig is.

De grootste wijziging was echter
de keuze voor een nieuwe programmeertaal. Waar het VIOE ontwikkelde in PHP en
`Ruimte en Erfgoed` over Java en .Net toepassingen beschikte, werd er besloten
om binnen het nieuwe agentschap te gaan voor `Python` als de voornaamste
programmeertaal. Binnen de `Python` webdevelopment wereld waren er op dat
moment 3 grote frameworks die konden gebruikt worden: `Django
<https://www.djangoproject.com>`_, `Flask <https://flask.pocoo.org>`_ en
`Pyramid <https://trypyramid.com>`_. Alle drie de frameworks werden onderzocht,
en uiteindelijk werd er besloten verder te gaan met het `Pyramid` framework.
Tenslotte werden er nog een aantal nieuwe technologieën toegevoegd aan het
eco-systeem. Om performant te kunnen zoeken in grote datasets werd de hulp van
`Elasticsearch <https://www.elastic.co>`_ ingeroepen. We begonnen te werken met
caches en queues in `Redis <https://redis.io>`_ voor asynchrone opdrachten.

Onze frontend pagina's maken sinds dan gebruik van een CSS framework zoals
`Foundation <https://foundation.zurb.com>`_. Net zoals heel veel andere
webontwikkelaars, hebben we ook de stap naar de `Single Page Applications` (SPA) 
gezet. Dit zijn webtoepassingen die heel sterk op een `Javascript` motor
draaien en continu communiceren met de backend server via netwerk calls. We
zetten die intensief in voor beheersomgevingen, complexe digitale omgevingen en
toepassingen zoals ons `geoportaal <https://geo.onroerenderfgoed.be>`_. Voor
openbare pagina's die vaak door het publiek geraadpleegd worden trachten we
deze altijd zo functioneel mogelijk te maken zonder veel nood aan Javascript
zodat deze maximaal kunnen werken op oudere toestellen en de inhoud goed
indexeerbaar is voor zoekmachines. Onze eerste SPA's werden nog ontwikkeld met
behulp van het `Dojo <https://dojotoolkit.org>`_ framework, onze recentere
toepassingen maken gebruik van het `Aurelia <https://aurelia.io>`_ framework.

Waar de oude inventaris in het begin nog draaide op een klassiek model van HTML
forms en HTTP POST requests, evolueerde die de voorbije tien jaar al
gedeeltelijk naar een systeem waarin webservices, meer bepaalde REST services,
een centrale rol speelden. In de nieuwe inventaris, net zoals in al onze andere
hedendaagse toepassingen, werd deze kaart resoluut getrokken. We hebben
hiervoor een `Resource Oriented Architecture` ontwikkeld waarin we overstappen
van enkele grote, monolithische toepassingen naar een systeem van kleinere,
meer gefocuste toepassingen die elk hun eigen specialisatie hebben. In 
:ref:`When Data Meets the Enterprise. <vdvemome2018>` 
gaan we hier uitgebreider op. De nieuwe inventaris vormt nu de centrale component
van het netwerk van toepassingen waarop het agentschap zijn werking uitbouwt.

Tenslotte ging het agentschap de voorbije jaren ook aan de slag met nieuwe
technologie voor het uitrollen en beheren van toepassingen. Waar we tien jaar
gelden nog manueel ingrepen deden op enkele servers in één datacenter, werken we
ondertussen met geautomatiseerde deploys in twee verschillende datacenters. Om
dit alles vlot werkbaar te houden, maken we gebruik van `Ansible` voor het
opzetten van basis servers en `fabric` voor het effectief uitrollen van
toepassingen. Alle databankschema's van toepassingen zitten in versie controle
en worden uitgerold met behulp van `Alembic`. Waar het uitrollen van een
toepassing tien jaar geleden nog een manueel proces was, is het nu een
semi-automatisch proces.

Niet enkel de technologie wijzigt
---------------------------------

Waar een belangrijk aantal wijzigingen van technologische aard waren, is ook de
inhoud en de focus daarvan de voorbije jaren sterk gewijzigd. Toen we in 2009
de inventaris lanceerden, waren we net het `Vlaams Instituut voor het Onroerend
Erfgoed` geworden. Een wetenschappelijke instelling van de Vlaamse Overheid die
voor het eerst al het onderzoek naar archeologie, bouwkundig erfgoed en
landschappen verenigde. Op dat moment kwamen een aantal inventarissen en
bijhorende informatiesystemen (databanken en in opbouw zijnde databanken, maar
ook boeken zoals Bouwen door de Eeuwen Heen) voor het eerst samen in beheer in
enkele organisatie. Omdat die verschillende systemen verschillende invalshoeken
en finaltiteiten kenden, werd de eerste versie van
`Inventaris Onroerend Erfgoed <https://inventaris.onroerenderfgoed.be>`_ 
geconcipieerd als een portaal. Daarop
wouden we de inventarissen samen ontsluiten, met één enkele look-and-feel, maar
elk met een eigen datamodel. De voornaamste raakpunten op dat moment waren
dat ze er een coherentere lijn werd gebracht in de GIS mogelijkheden, dat ze
een beeldbank deelden en dat er relaties konden gelegd werden tussen
verschillende objecten in verschillende inventarissen die misschien geheel of
gedeeltelijk hetzelfde object in de realiteit zijn. Bij de lancering in mei
2009 bevatte het portaal de inventaris van het bouwkundig erfgoed en de
inventaris wereldoorlog erfgoed. Daarnaast waren er ondersteunende modules voor
afbeeldingen, gebeurtenissen en thesaurustermen.

Tussen 2009 en 2015 werden nieuwe modules toegevoegd aan het portaal: de
inventaris van orgels, archeologische zones, historische tuinen en parken,
houtige beplantingen met erfgoedwaarde, de ankerplaatsen uit de
landschapsatlas en het varend erfgoed. Waar we er op voorhand van uit gingen
dat elk van deze inventarissen een heel eigen datamodel had, bleek dit in de
parktijk niet zo te zijn. Er konden een aantal verschillen in methodiek
vastgesteld worden, die soms aanleiding geven tot verschillen in terminologie
(een gebouw wordt gesloopt, een boom wordt gerooid), maar de essentie bleef
dezelfde. Beschrijven welk erfgoed zich waar bevindt en dat erfgoed
documenteren met afbeeldingen, beschrijvingen, trefwoorden (thesaurustermen),
... Waar het steeds op neerkomt: wat ligt waar, wat is het en hoe oud is het en
waarom is het belangrijk? Elke nieuwe module die werd toegevoegd kreeg dan ook
de vorm van een aangepaste versie van de inventaris bouwkundig erfgoed. Het
voornaamste verschil dat bleef bestaan, zat in de locatiecomponent van de
inventarissen. Die voor bouwkundig erfgoed was gericht op zeer accurate
adresgegevens van kleine erfgoedelementen (met een focus op individuele
adressen), de andere modules ware meer gericht
op grote erfgoedgehelen (met een focus op groepen of clusters van adressen). 

Toen het VIOE samengevoegd werd met het
agentschap Ruimte en Erfgoed in 2012, kwam ook de databank van het beschermd
erfgoed naar het agentschap. Bij de eerste analyses bleek dat die databank
vooral bestond uit juridische gegevens en weinig inhoudelijke informatie kende.
Daarom werd besloten de informatie uit de beschermingsdatabank toe te voege aan
de inventaris in een aparte module. Ook deze deelde grotendeels het datamodel
van de inventaris. Uiteindelijk mondde dit uit in de dataset van de
aanduidingsobjecten. (:ref:`inventaris-erfgoedobjecten-aanduidingsobjecten`)
Deze werd in juni 2016 openbaar gemaakt.

Tijdens de levensloop van de inventaris werd zo langzaam duidelijk dat al die
verschillende inventarissen helemaal niet zo verschillend waren. Op een paar
kleine verschillen na, bleken er veel meer gelijkenissen dan verschillen te
zijn. We begonnen de inventaris dan ook meer als een geïntegreerde inventaris
te zien. Het digitaliseren van de verschillende inventarissen leidde tot meer
communicatie en overeenstemming tussen de verschillende erfgoedonderzoekers en
een intensere samenwerking (:ref:`On data-driven systems and system-driven data <vdmemo2016>`).

Samen met de lancering van de beschermingsdatabank als de
aanduidingsobjecten, lanceerden we de term erfgoedobjecten
(:ref:`inventaris-erfgoedobjecten-aanduidingsobjecten`). Elk van de
objecten uit de wetenschappelijke inventarissen werd een erfgoedobject met een
eigen URI. In 2016 waren dit nog grotendeels kosmetische oplossingen. De
verschillende detailpagina's werden samengevoegd tot 1 pagina waarbij elk van
de erfgoedobjecten op een uniforme manier gepresenteerd werd. Achterliggend
waren dit echter nog steeds verschillende datasets met een eigen datamodel.

Zo werd er gestart met de voorbereidingen van wat uiteindelijk de nieuwe
inventaris zou worden. Enerzijds omdat onze visie op de verschillende
wetenschappelijke inventarissen de voorbije jaren sterk gewijzigd is, van
allemaal aparte silo's naar één grote inventaris van erfgoedobjecten.
Anderzijds omdat de technologische componenten van de inventaris aan
vervanging toe waren.

Iedereen die de IT wereld kent, weet dat deze nog steeds snel evolueert. Onze
core business is dan misschien het verleden, we willen dat verleden wel op een
toekomstgerichte manier beheren. Dat vereist een continue, adaptieve aanpak
waarbij we steeds open staan voor nieuwe initiatieven en mogelijkheden die
optreden. Dat gaat van nieuwe inzichten in onze eigen materie, het onroerend
erfgoed, tot nieuwe inzichten in de technologie die 
we gebruiken om dat erfgoed digitaal te ontsluiten en beheren. Heb je vragen 
over hoe dit in zijn werk gaat, `aarzel dan niet ze te stellen <ict@onroerenderfgoed.be>`_.
