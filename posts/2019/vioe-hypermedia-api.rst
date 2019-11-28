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
https://informatievlaanderen.github.io/handreikingOslo/`_ taskforce. This 
taskforce creates standards, semantic models and tooling for Flemish government agency 
and other connected partners. One of the projects that ran in 2018, was the
creation of a `Generic Hypermedia API <https://github.com/Informatievlaanderen/generieke-hypermedia-api>`_ 
standard, a set of guidelines and building blocks that aim to transform REST
services into more Hypermedia driven services that would be more interoperable.
The first version of this standard was approved on november 8, 2018 and
contains three building blocks: language, CRUD and pagination.

At Flanders Heritage, we have started aligning our information systems with
this new standard, especially the `pagination` building block. For the moment
we are striving towards adopting the HTTP Link header method of pagination, as
specified by
https://github.com/Informatievlaanderen/generieke-hypermedia-api/blob/master/paginering.md#http
and detailed in https://tools.ietf.org/html/rfc5988.

https://bib.onroerenderfgoed.be/werken?titel=knokke

.. code-block::
    
    <https://bib.onroerenderfgoed.be/werken?titel=knokke&per_pagina=10&pagina=2>; rel="next", <https://bib.onroerenderfgoed.be/werken?titel=knokke&per_pagina=10&pagina=17>; rel="last", <https://bib.onroerenderfgoed.be/werken?titel=knokke&per_pagina=10&pagina=1>; rel="first"

