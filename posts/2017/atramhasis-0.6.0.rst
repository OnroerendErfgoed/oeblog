.. post::
   :category: releases, thesaurus, open source
   :tags: atramhasis
   :author: Koen Van Daele
   :language: en

Atramhasis v0.6.0 released
==========================

A new version (0.6.0) of :pypi:`Atramhasis <atramhasis>` has been released.
Atramhasis is an open-source, web-based SKOS editor. You can use it to browse
SKOS vocabularies, thesauri, authority files, word lists, ... Atramhasis 
comes with an admin interface you can use to add the concepts and collections of
your vocabularies. To make integrating vocabularies with your other IT systems
easy, all data in Atramhasis is exposed through a read an write REST webservice.

This release is a major update based on the :pypi:`Skosprovider <skosprovider>`
0.7.0 line of libraries. The major new features of this release have to do with
Linked Data. It is now possible to have Atramhasis create nightly dumps per
conceptscheme. Before, they had to be created on the fly. Which was a rather
costly operation for larger conceptschemes. Using these nightly dumps it's now
very easy to run your own `Linked Data Fragments server <https://linkeddatafragments.org>`_.
The new version can generate a config file for such a server that you can use to 
setup the server. By default this config will work with the Turtle files that can
be generated every night. But if you have access to the
`https://github.com/rdfhdt/hdt-cpp <HDT library>`_, you can also work with HDT 
files for a masssive performance boost. See the section `Running a Linked
Data Fragments server` in the `Atramhasis documentation
<https://atramhasis.readthedocs.io>`_ for more information.

Other minor enhancements were added as well. It's now possible to have
Atramhasis generate URI's for concepts when importing a conceptscheme on the
commandline. Previously, if you imported a `CSV` or `JSON` file that didn't
contain URI's, they would be generated using a default pattern that ensured
internal data integrity but was never the right pattern for the user. It is now
possible to specify such a pattern when importing. If for some reason, this is
not sufficient, users are advised to generate the URI's before importing as
Atramhasis will respect those.

A new type of labels callel sortlabels have also been added. Users can add these
to concepts and collections to make it possible to apply custom sorting
strategies. Most thesauri are seen as textual in nature and users expect these
to be sorted alphanumerically. But some thesauri are different. Flanders Heritage
has a list of `historic periods
<https://thesaurus.onroerenderfgoed.be/conceptschemes/DATERINGEN>`_. For a
conceptscheme like this, alphanumerical sorting makes little sense. Most people
want to see this conceptscheme sorted chronologically. Th expect `Roman` to be 
listed before `Medieval`. While version 0.6.0 does not yet show this sort order
in the public user interface, you can now start applying sortlabels. By creating
a special label you can thus force the order of concepts. For the moment this is
already accessible through the REST interface, future version will apply this
logic to the tree view as well. It might be important to note that these work
like other labels as well, so they are language dependent as well.

As always, bugs have been fixed, code has been 
rewritten and documenation has been updated. See
https://github.com/OnroerendErfgoed/atramhasis/releases/tag/0.6.0 for the full
list of changes.

We invite everybody to try out the release. You can see a working example of
Atramhasis at https://thesaurus.onroerenderfgoed.be, a customised version of
Atramhasis containing the thesauri use by `Flanders Heritage Agency <https://www.onroerenderfgoed.be>`_.
If you encounter problems, please let us know. Either through the 
`forum <https://groups.google.com/forum/#!forum/atramhasis>`_ or our 
`Github tracker <https://github.com/OnroerendErfgoed/atramhasis>`_.
