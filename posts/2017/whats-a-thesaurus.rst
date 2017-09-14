.. post:: 2017-09-14
   :category: thesaurus
   :tags: vocabulary, indexing, search
   :author: Koen Van Daele
   :language: en

What's a thesaurus?
===================

We recently released a new version of Atramhasis (:ref:`atramhasis-0.6.0`), our
web based thesaurus editor. But what is a thesaurus and why would a heritage
organisation want one?

Our colleagues at `Historic England <http://www.historicengland.org.uk>`_ define 
a thesaurus as *A structured wordlist used to standardize terminology. It is used 
to assist in indexing and retrieving information within databases that make use 
of the same terminology*. A lot of opportunities arise from structuring related
terms.

First of all, it is possible to express equivalencies. Defining what terms are
equivalent makes it easier to find what one is looking for. This used to be done 
by stating that two terms are synonyms. Nowadays it’s more common to state that 
both terms are verbal expressions of the same concept. While before we would
have stated that *Jugendstil* is equal to *Art Nouveau*, today we would say that
there is a concept of a certain artistic style that is labelled with both
*Jugendstil* and *Art Nouveau*. A fairly subtle difference that mainly impacts
how you interact with thesauri.

Secondly, there are hierarchical relationship. Typically this is done by stating
that one term is broader than another and correspondingly that the other term is
narrower than the first one. This makes it possibkme in a thesaurus to
state that a cathedral is a church and that a church is a religious building.
From this we can conclude that cathedrals are religious buildings as well. It is 
important to note that not all hierarchical relations in thesauri are of the 
*is a* type. *Is part of* and *Is an instance of* relations exist 
as well. They do complicate certain matters, so be careful when considering them.
Consult `On the composition of ISO 25964 hierarchical relations (BTG, BTP, BTI)
<https://link.springer.com/article/10.1007/s00799-015-0162-2>`_ to see how they 
affect the whole of the relations between terms in your thesaurus.

The final type of relationship is the associative relationship. This is the
*softest* relationship, stating that two terms or concepts are related. This
might be *coal mine* is related to *miner’s houses* because in Flanders every
coal mine had it’s own little town where all the mineworkers lived together.

One other important aspect of thesauri is that they allow defining a scope note.
This is a written definition of the concept and how it should be used in
databases. It’s a critical feature that allows users to evaluate if a certain
concept actually means what they think it means. Over the years, we have found
that asking experts to define concepts they thought were self-evident has caused
heated discussions. As long as you don't define what something means everyone
can use a concept in the way they want to use it and ignore the fact that not
everyone might share their opinion.

So, thesauri allow us to reach consenus on the meaning of certain concepts and
share our knowledge about these concepts with the outside world (that's why we
publish them as open data). But we do have another, very pratical, reason for
building and maintaining them. We use these controlled to help indexing our main
databases and information systems. When you go searching for 
`fountains <https://inventaris.onroerenderfgoed.be/erfgoedobjecten?typologie=fonteinen>`_ 
in our inventory management system, our thesaurus is used. When the inventory
receives the query for *fountains* it checks if it's actually in the thesaurus.
If not, no record can be indexed with that term, so it stops the search. If it
is, the system checks if there are more specific version of fountains present in
the thesaurus. In this case, there's also a concept of *water tricks* that is
defined as a specific type of fountain. So, when our inventory management
systems answers you query for fountains it gives you all records indexed as *fountains* 
or as *water tricks*.

Interestingly enough, those *water tricks* also demonstrate another handy
feature of our thesauri. If you look at the record for `water tricks
<https://id.erfgoed.net/thesauri/erfgoedtypes/1524>`_ you will notice we call
them *bedriegertjes* in Dutch, but do not actually have an English label for
them. Luckily, we have linked our concept of *bedriegertjes* with the concept of
*bedriegertjes* in the `Art & Architecture Thesaurus <http://www.getty.edu/research/tools/vocabularies/aat/>`_. 
This huge thesaurus tells us that *bedriegertjes* are known in English as *water
tricks* or *joke fountains*.. It even tells us what they are called in German
and Spanish. Opening us up to wealth of possible interactions with other
systems.

In the end, theauri are a means. Not an end. Our prime concern is managing
heritage, not building thesauri. But they do help us tremendously in defining
what that heritage is, in searching through that heritage and in linking the
heritage on our local level to the transnational level. If you want to know more
about our thesauri, have a look at :ref:`Calling it what it is <movdme2017>`,
where we explain how we built them and provide you with some do's and don'ts.
