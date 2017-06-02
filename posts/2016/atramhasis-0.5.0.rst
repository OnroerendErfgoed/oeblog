.. post:: 2016-09-14
   :category: releases, thesaurus, open source
   :tags: atramhasis
   :author: Koen Van Daele
   :language: en

Atramhasis v0.5.0 released
==========================

A new version (0.5.0) of :pypi:`Atramhasis <atramhasis>` has been released.
Atramhasis is an open-source, web-based SKOS editor. You can use it to browse
SKOS vocabularies, thesauri, authority files, word lists, ... Atramhasis also
comes with an admin interface you can use to add the concepts and collections of
your vocabularies.

This release is a major update based on the :pypi:`Skosprovider <skosprovider>`
0.6.0 line of libraries. The most visible change is with the public and admin
interfaces. These have been completely overhauled to provide a more pleasing
userexperience. Among other things visitors are now pointed towards popular
concepts and concepts they have recently visited. Browsing an entire conceptscheme
tree has been redesigned.

The admin interface now offers users an option to edit certain aspects of a
conceptscheme such as the labels, notes and sources. Editing in general has been
update and improved. Links between the public interface and the admin interface
have been added to make switching from one to the other easier. Notes and
sources can now contain certain HTML tags, allowing greater flexibility in
defining concepts and collections.

A command line script was added to make it easy to import an entire
conceptscheme, eg. when migrating from another system. It is now possible to
import a RDF, CSV or JSON file on the command line in your Atramhasis instance.
With earlier versions you had to script this yourself.

As always, bugs have been fixed, code has been rewritten and documenation has
been updated. See
https://github.com/OnroerendErfgoed/atramhasis/milestone/8?closed=1 for the full
list of changes.

We invite everybody to try out the beta release. The public frontend can be
found at http://glacial-bastion-1106.herokuapp.com/. For the admin backend, go
to http://glacial-bastion-1106.herokuapp.com/admin. Please login using a
Mozilla Persona account. You will have full access to the admin. If you
encounter problems logging in, please let us know. Either through this forum or
our `Github tracker <https://github.com/OnroerendErfgoed/atramhasis>`_.
