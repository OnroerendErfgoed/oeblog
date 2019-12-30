.. post:: 
   :category: services
   :tags: API, hypermedia
   :author: Koen Van Daele
   :language: en

We are the Hypermedia!
======================

Within the Flemish Government, there is a central governing body that
coordinates matters on Information and ICT policies. Under the umbrella of this
body, several taksforces exist, one of them being the `OSLO Datastandards
<https://informatievlaanderen.github.io/handreikingOslo/>`_ taskforce. This 
taskforce creates standards, semantic models and tooling for Flemish government agency 
and other connected partners. One of the projects that ran in 2018, was the
creation of a `Generic Hypermedia API <https://github.com/Informatievlaanderen/generieke-hypermedia-api>`_ 
standard, a set of guidelines and building blocks that aim to transform REST
services into more Hypermedia driven services that would be more interoperable.
The first version of this standard was approved on november 8, 2018 and
contains three building blocks: language, CRUD and pagination.

Pagination. Web scale
---------------------

At Flanders Heritage, we have started aligning our information systems with
this new standard, especially the `pagination` building block. For the moment
we are striving towards adopting the HTTP Link header method of pagination, as
specified by
https://github.com/Informatievlaanderen/generieke-hypermedia-api/blob/master/paginering.md#http
and detailed in https://tools.ietf.org/html/rfc5988.

If we want to see this in action, we need to link at the `Link` http header.
There are several ways to do this. You can use a commandline tool such as curl,
a web browser plugin or a standalone REST client. Whichever one you use, should
be able to show you this information. In our examples we'll be using CURL, a
tool that is generally present or easy to install on a Linux or Mac computer.

Suppose we are interested in books and documents about `Knokke`, a coastal town
in Flanders. We can do this by using the REST api at
https://bib.onroerenderfgoed.be/api_docs. This teaches us that we can call 
https://bib.onroerenderfgoed.be/werken with the `titel` parameter. So, 
https://bib.onroerenderfgoed.be/werken?titel=knokke gives us books that contain
`Knokke` in the title or have a chapter that contains it in the title:

.. code-block::

    $ curl -G -i -H Accept:application/json https://bib.onroerenderfgoed.be/werken?titel=knokke
    HTTP/1.1 200 OK
    Date: Mon, 16 Dec 2019 19:51:07 GMT
    Server: Apache
    Content-Type: application/json
    Content-Length: 3933
    Access-Control-Expose-Headers: Content-Range, X-Content-Range
    Accept-Ranges: items
    Content-Range: items 0-9/167
    Link: <https://bib.onroerenderfgoed.be/werken?titel=knokke&per_pagina=10&pagina=2>; rel="next", <https://bib.onroerenderfgoed.be/werken?titel=knokke&per_pagina=10&pagina=17>; rel="last", <https://bib.onroerenderfgoed.be/werken?titel=knokke&per_pagina=10&pagina=1>; rel="first"
    X-Content-Type-Options: nosniff
    Access-Control-Allow-Origin: *
    Set-Cookie: BIGipServerPOOL-AUTO-vioe-informatiecatalogus-prod-std=456599562.20480.0000; path=/; Httponly
    X-Permitted-Cross-Domain-Policies: none
    X-XSS-Protection: 1; mode=block

    [{"publicatietype": {"url": "http://purl.org/ontology/bibo/Document", "naam": "Document", "id": 1}, "titel": "Het landelijke Knokke", "self": "https://bib.onroerenderfgoed.be/werken/552291", "uri": "https://id.erfgoed.net/infocat/werken/552291", "serie": {"naam": "GEEN SERIE", "id": 0}, "auteur": "D'hont A.", "id": 552291, "omschrijving": "Het landelijke Knokke"}, {"jaar": "2011", "publicatietype": {"url": "http://purl.org/ontology/bibo/Document", "naam": "Document", "id": 1}, "titel": "Duin&Water, Knokke", "self": "https://bib.onroerenderfgoed.be/werken/545629", "uri": "https://id.erfgoed.net/infocat/werken/545629", "serie": {"naam": "GEEN SERIE", "id": 0}, "auteur": "Decraemer S.", "id": 545629, "omschrijving": "Duin&Water, Knokke"}, {"jaar": "1976", "publicatietype": {"url": "http://purl.org/ontology/bibo/Document", "naam": "Document", "id": 1}, "titel": "Dagklapper uit Knokke", "self": "https://bib.onroerenderfgoed.be/werken/552280", "uri": "https://id.erfgoed.net/infocat/werken/552280", "serie": {"naam": "GEEN SERIE", "id": 0}, "auteur": "D'Hont A.", "id": 552280, "omschrijving": "Dagklapper uit Knokke"}, {"jaar": "2006", "publicatietype": {"url": "http://purl.org/ontology/bibo/Document", "naam": "Document", "id": 1}, "titel": "Een casino voor de toekomst", "self": "https://bib.onroerenderfgoed.be/werken/545165", "uri": "https://id.erfgoed.net/infocat/werken/545165", "serie": {"naam": "GEEN SERIE", "id": 0}, "id": 545165, "omschrijving": "Een casino voor de toekomst"}, {"jaar": "2004", "publicatietype": {"url": "http://purl.org/ontology/bibo/Document", "naam": "Document", "id": 1}, "titel": "Knokke-Heist natuurlijk", "self": "https://bib.onroerenderfgoed.be/werken/552299", "uri": "https://id.erfgoed.net/infocat/werken/552299", "serie": {"naam": "GEEN SERIE", "id": 0}, "auteur": "Struyf K.", "id": 552299, "omschrijving": "Knokke-Heist natuurlijk"}, {"jaar": "2000", "publicatietype": {"url": "http://purl.org/ontology/bibo/Document", "naam": "Document", "id": 1}, "titel": "Knokke-Heist geboekstaafd", "self": "https://bib.onroerenderfgoed.be/werken/552277", "uri": "https://id.erfgoed.net/infocat/werken/552277", "serie": {"naam": "GEEN SERIE", "id": 0}, "id": 552277, "omschrijving": "Knokke-Heist geboekstaafd"}, {"jaar": "2001", "publicatietype": {"url": "http://purl.org/ontology/bibo/Document", "naam": "Document", "id": 1}, "titel": "Nellens Albertstrand Casino Knokke", "self": "https://bib.onroerenderfgoed.be/werken/552290", "uri": "https://id.erfgoed.net/infocat/werken/552290", "serie": {"naam": "GEEN SERIE", "id": 0}, "auteur": "D'hont A.", "id": 552290, "omschrijving": "Nellens Albertstrand Casino Knokke"}, {"jaar": "2007", "publicatietype": {"url": "http://purl.org/ontology/bibo/Document", "naam": "Document", "id": 1}, "titel": "Archeologisch onderzoek op de hoek van de Kursaalstraat en de Kerkstraat te Knokke-Heist", "self": "https://bib.onroerenderfgoed.be/werken/534021", "uri": "https://id.erfgoed.net/infocat/werken/534021", "serie": {"naam": "GEEN SERIE", "id": 0}, "id": 534021, "omschrijving": "Archeologisch onderzoek op de hoek van de Kursaalstraat en de Kerkstraat te Knokke-Heist"}, {"jaar": "2010", "publicatietype": {"url": "http://purl.org/ontology/bibo/Document", "naam": "Document", "id": 1}, "titel": "Verstild versteend verleden", "self": "https://bib.onroerenderfgoed.be/werken/536850", "uri": "https://id.erfgoed.net/infocat/werken/536850", "serie": {"naam": "GEEN SERIE", "id": 0}, "id": 536850, "omschrijving": "Verstild versteend verleden"}, {"jaar": "1985", "publicatietype": {"url": "http://purl.org/ontology/bibo/Document", "naam": "Document", "id": 1}, "titel": "Het Knokke van toen", "self": "https://bib.onroerenderfgoed.be/werken/13455", "uri": "https://id.erfgoed.net/infocat/werken/13455", "volume": "14", "serie": {"naam": "Het \"Dorp\" van toen", "id": 499957}, "auteur": "LANNOY Danny", "id": 13455, "omschrijving": "Het Knokke van toen"}]


This :command:`curl` command fetches books and documents (`werken`) from 
our library catalog that have `knokke` in the title. We also ask it to print
the headers. Within those headers, we care about the `Link` header in this
case.

.. code-block::
    
    Link: <https://bib.onroerenderfgoed.be/werken?titel=knokke&per_pagina=10&pagina=2>; rel="next", <https://bib.onroerenderfgoed.be/werken?titel=knokke&per_pagina=10&pagina=17>; rel="last", <https://bib.onroerenderfgoed.be/werken?titel=knokke&per_pagina=10&pagina=1>; rel="first"


While we
immediately get some results back, this is only a partial result set. When we
look at the `Link` header, it tells us there are more pages of results. There's
a `next` page, a `last` page and a `first` page. Since we're currently at page
1, there's no `previous` page. By following the links here, we can either keep
on requesting the next page or we can jump straight to the last page. It's
important to note that the client should not assume anything about the links
it's getting back. We might be tempted to calculate that if there
are 17 pages and each pages contains at most 10 records, there are between 161
and 170 results. But the server is not obliged to put any of this information
in the link or to honor anything about it. The link should treated as just
that, a link, and it could just have well been something that is not
interpretable. This does reveal one major weakness of using the `Link` header
for pagination purposes, there's no mechanism to indicate how manty results
the are or how many links the client will need to follow to reach the end of
the result set. AS far as the client is concerned, there's a next link and a
last link. If there's no next link, we're at the last page and if
the next and last links are identical, we're at the last-but-one page. But
there's no way to discern when we're in the middle how far away we are from the
end. On the other hand, our client needs no knowledge whatsoever of the
structure inherent in our URL's. It does not need to understand if there's a
`page` or a `pagina` parameter or `limit` and `offset` parameters or other
simiar mechanisms for pagination. This allows us to reuse client code for lots
of different webservices. All the client needs to know is that if there's a
`next` link, it can fetch more results.

So, if we now want to fetch the second page of results, we use this command:

.. code-block::

    $ curl -G -i -H Accept:application/json https://bib.onroerenderfgoed.be/werken?titel=knokke\&per_pagina=10\&pagina=2

All your data belongs to us!
----------------------------

To demonstrate this, we have written a small Python script that queries several 
of our information systems for information and handles all pagination of results
through the `Link` header. In Python, it's common to use the 
`requests <https://requests.readthedocs.io/en/master/>`_ library
for doing calls to REST services. It turns out that we're even more fortunate,
since `requests` has built in support for the `Link` header. This makes it dead
simple to iterate over all the results. For this little excercise, we're
fetching all the images, erfgoedobjecten, aanduidingsobjecten and themas from
the municipality of `Knokke-Heist`. It takes very little effort to write and
delivers a mass of URI's at our feet.

.. literalinclude:: link_header.py
    :language: python

If we execute this command, we now get a big, long list of URI's on our screen.
It works perfectly, but it's not that satisfying. A URI might be good for a
machine, but we don't really know what it represents. So, what can we do?

No context, no information
--------------------------

Another interesting technique in the Linked Data world is called `JSON-LD (JSON
for Linking Data) <https://json-ld.org>`_. It allows us to turn plain old JSON into linked data and 
make our objects more compatible. The basic idea is that we map our JSON dataset
to actual RDF objects by defining a `context`. In this context, we map keys in 
our JSON to RDF properties. As an example, here's a simple context that can be 
used on our image database endpoint:

.. code-block:: json-ld

    {
        "dct": "http://purl.org/dc/terms/",
        "title": "dct:title",
        "description": "dct:description",
        "uri": "@id"
    }

This context defines a namespace shorthand, `dct`, and maps it to the Dublin
Core Terms namespace `http://purl.org/dc/terms/`. It allows us to write
`dct:title` as shorthand for `http://purl.org/dc/terms/title`. We have also
defined `uri` to be an alias for `@id`. `@id` in JSON-ld indicates the
unique identifier for a certain record or resource. Applying this context to an
image from our image database gives us the following JSON data:

.. code-block:: json-ld

    {
        "@id": "https://id.erfgoed.net/afbeeldingen/392715",
        "http://purl.org/dc/terms/title": "Villa Cools met kinesistenpraktijk",
        "http://purl.org/dc/terms/description": "",
    }

This tells us there's a resource with the id `https://id.erfgoed.net/afbeeldingen/392715`
that can be described with a `title` from the Dublin Core Terms vocabulary.
Quite common in JSON-LD would be to assign a type to the resource we're talking
about. We might know this record comes from the image database, but it's
currently not reflected in our data. Once we add data from the inventory we
might not be able to tell the difference anymore. In JSON-LD we would add an 
`@type` key and set it to the URI of a class from an RDF vocabulary like this:

.. code-block:: json-ld

    {
        "@id": "https://id.erfgoed.net/afbeeldingen/392715",
        "@type": "http://purl.org/dc/dcmitype/Image",
        "http://purl.org/dc/terms/title": "Villa Cools met kinesistenpraktijk",
        "http://purl.org/dc/terms/description": "",
    }

Once More, with Feeling
-----------------------

We'll use JSON-LD to enhance our script. We want to homogenise our dataset of
all information from `Knokke-Heist` so we are left with only records having the
same structure. We've made two JSON-LD contexts, one for the image database and
a second one for the three datasets originating from our inventory since their
datamodels are extremely similar. The datasets don't normally include the type
of resource they contain but we do want to be able to tell the difference in
our final dataset, so we'll add those here. Our inventory systems have a field
called `locatie_samenvatting` that provides a summary of the geographic
location of an object. While the summary algorithm can be fairly complicated
(there's things that are located in more than one street in more than one
municiaplity or even more than one province), it's very useful for a human to
quickly see where something can be found. There's no such field in the image
database and we've created a quick replacement for the dataset (luckily the
location of images is much simpler than that of heritage objects).

Our script fetches all data like before, but we now add the type of record
we're fetching and for images we add a simple location summary. Then we
expand all of them into JSON-LD using the `pyLD
<https://pypi.org/project/PyLD/>`_ Python library. This leaves us with a
dataset that is valid JSON-LD, but a bit unwieldy. Every key in the dataset is
now identical, but it is a URI, which is not very practical. So, we'll simplify 
things for ourselves, again using JSON-LD. We've defined a third context based on 
the Dublin Core Terms vocabulary we'll use to compact our existing JSON-LD. 
Finally we print them to the screen.

.. literalinclude:: link_header_jsonld.py
    :language: python

To run this script, don't forget to install the `requests` and `pyLD`
libraries. If you now run this script, you should see a whole list of
information printed to the screen. It make take a while though, especially for
the large municipalities like `Gent` or `Antwerpen`. As a little encore, we've
added another version of this script that doesn't print to the screen, but writes
our new dataset to a csv for further processing.

.. literalinclude:: link_header_jsonld_csv.py
    :language: python

If you're interested in things such as Hypermedia API's and Linked Data, be
sure to check out https://data.vlaanderen.be/ as it contains much more
information about these topics and points you to all the relevant documents and
standards. There's a whole community of people knowledgeable about Linked Data
out there who are more than willing to answer your questions, you'll find quite
a few of them on `Twitter <https://twitter.com/koenedaele/lists/linked-data>`_.
As always, feel free to `contact us <ict@onroerenderfgoed.be>`_ with further
questions.
