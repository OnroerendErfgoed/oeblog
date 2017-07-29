.. post::
   :category: releases, thesaurus, open source
   :tags: atramhasis
   :author: Koen Van Daele
   :language: en

Atramhasis v0.6.0 released
==========================

A new version (0.6.0) of :pypi:`Atramhasis <atramhasis>` has been released.
Atramhasis is an open-source, web-based SKOS editor. You can use it to browse
SKOS vocabularies, thesauri, authority files, word lists, ... Atramhasis also
comes with an admin interface you can use to add the concepts and collections of
your vocabularies.

This release is a major update based on the :pypi:`Skosprovider <skosprovider>`
0.7.0 line of libraries. The major new features of this release have to do with
Linked Data. It is now possible to have Atramhasis create nightly dumps per
conceptscheme. Before, they had to be created on the fly. Which was a rather
costly operation for larger conceptschemes. Using these nightly dumps it's now
very easy to run your own `Linked Data Fragments server <https://linkeddatafragments.org>`_.
Atramhasis can now generate a config file for such a server that you can use to 
setup the server. By default this config will work with the Turtle files that can
be generated every night. But if you have access to the
`https://github.com/rdfhdt/hdt-cpp <HDT library>`_, you can also work with HDT 
files for a masssive performance boost. See the section `Running a Linked
Data Fragments server` in the docs for more information.

As always, bugs have been fixed, code has been rewritten and documenation has
been updated. See
https://github.com/OnroerendErfgoed/atramhasis/releases/tag/0.6.0 for the full
list of changes.

We invite everybody to try out the release. You can see a working example of
Atramhasis at https://thesaurus.onroerenderfgoed.be, a customised version of
Atramhasis containing the thesauri use by `Flanders Heritage Agency <https://www.onroerenderfgoed.be>`_.
If you encounter problems, please let us know. Either through the 
`forum <https://groups.google.com/forum/#!forum/atramhasis>`_ or our 
`Github tracker <https://github.com/OnroerendErfgoed/atramhasis>`_.
