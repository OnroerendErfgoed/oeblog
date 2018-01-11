.. post:: 2018-01-11
   :category: thesaurus, open source
   :tags: atramhasis
   :author: Maarten Vermeyen, Koen Van Daele
   :language: en

Running an Atramhasis demo site with Docker
===========================================

`Atramhasis <http://atramhasis.readthedocs.io/>`_ is an online SKOS editor.
It allows a user to create and edit an online thesaurus (:ref:`whats-a-thesaurus`)
or vocabulary adhering to the `SKOS specification <skos_spec_>`_ through a
simple web interface. This allows any user with access to a web browser to
consult the thesauri and if so wanted AND authorised, to edit them.

While it used to be a bit of work to set up a demo instance of Atramhasis, we
have now provided a `Docker image <https://hub.docker.com/r/atramhasis/demo/>`_
available that allows you to quickly get a demo instance up and running.
The Docker image contains both a demo application and the related
`Linked Data Fragments <ldf_>`_ server.

After `installing Docker for your operating system
<https://docs.docker.com/engine/installation/#supported-platforms>`_ (the CE
edition works is more than sufficient for this), you
can simply pull the image and run a container. Once you've
executed the following commands, you should be able to
visit the demo application in your browser on
`<http://localhost:6543>`_. A Linked Data Fragments server is also included
in the demo, which is accessible on `<http://localhost:3000>`_.

.. code::

   $ sudo docker pull atramhasis/demo
   $ sudo docker run -p 6543:6543 -p 3000:3000 atramhasis/demo

Alternatively, you can run a specific version of Atramhasis
(starting from atramhasis 0.6.4):

.. code::

   $ sudo docker pull atramhasis/demo:0.6.4
   $ sudo docker run -p 6543:6543 -p 3000:3000 atramhasis/demo:0.6.4

While this is a fast and easy way to get a first impression of
Atramhasis, please be aware  that any edits you make when running the
image, will be discarded when you stop the Docker container. If you want
to test the application over a longer period of time, this is probably not
what you're looking for. If you need persistence, but still want to use
Docker, you can customise the
`Dockerfile <https://github.com/OnroerendErfgoed/atramhasis-demo-docker/>`_
to suit your needs.

.. _skos_spec: http://www.w3.org/TR/skos-reference/
.. _ldf: http://linkeddatafragments.org/
