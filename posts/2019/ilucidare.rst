.. post:: 2019-11-20
   :category: GIS
   :tags: innovation, geoportaal, beeldbank, OAR
   :author: Koen Van Daele
   :language: en

Welcome to the Ilucidare Playground
===================================

Today (2019-11-20), we are present at the `Ilucidare Playground: Cracking the
future of heritage <https://ilucidare.eu>`_. Members of `Flanders Heritage Agency's
<https://www.onroerenderfgoed.be>`_ Information Team will show some 
aspects of our how we are mixing heritage and technology on a daily 
basis. The Information team consists of specialist staff trained in IT
and Information Management. They are IT professionals from different
backgrounds that run our daily IT operations, IT program management,
application development, system and data management who work together with
professionals in information management that run analog and digital archives,
image databases, the library and documentation center and our online
repository of open access publications. While this team has a vast
array of responsibilities and duties, today we'll focus on a few key
examples that show how well heritage, technology and digitisation match.

No innovation without dissemination
-----------------------------------

As important as innovation is, it has little value if the output of that
innovation does not reach our colleagues, heritage professionals, or the
general public. Both Flanders Heritage and the wider Flemish Government
have taken a stance for open data and open access. For Flanders Heritage this
means that we strive to make as much of our publications available under the
Flemish Open Data license or other licenses if applicable. All research output
we can publish gets published at `OAR, our Open Access Repository <https://oar.onroerenderfgoed.be>`_.
The past years we have invested in digitising most publications by our
predecessors. We now have an online publication archive going back to the
eighties that can be freely downloaded and accessed. While this might seem like
a trivial matter, it has taken quite a lot of time and effort. We have found
that in today's digital world, knowledge and information are at risk of
becoming obsolete if not available in the way people expect them to be. By
digitising older information sources, we give them that little push, that
little bit of innovation, to make them relevant in today's roaring digital
twenties. Our download statistics prove that this has very much been
appreciated. Ever since we published our back catalogue, the number of
downloads per month has doubled. We now have about 15.000 publications that are
digitally consulted every month.

.. image:: ilucidare_oar_downloads_per_month.png

*Number of downloads per month from OAR*

Pictures or it didn't happen
----------------------------

While our publications are still very much an information channel that spreads
textual information, today an increased importance is placed on visual
information. Where 20-30 years ago digital mostly meant textual information
(anybody remember ASCII art?), today a lot of emphasis is placed on digital
media: audio, video and images (mostly of cats). While audio and video is
still a fairly rare format for us, images have always been a staple in our
information diet. Heritage professionals have been documenting heritage and
it's current state ever since camera's became available. The rise to prominence
of digital camera's and more recently smartphones with a good camera has only
accelerated this process. We estimate that within our agency a few million
pictures are circulating in both analog and digital formats. In 2019 we
launched a new online `image database <https://beeldbank.onroerenderfgoed.be>`_
containing some 280.000 images of heritage in Flanders. Some of them recent,
some of them digitised from analog sources in our archives. Again, a lot of
importance was placed on reuseability. Where possible, they are published under
an open data license allowing reuse, even for commercial purposes, as long as
attribution is guaranteed.

.. image:: ilucidare_images_bijloke.png

*A set of images in the image database found by searching for `Bijloke`*

Now we have our basic system in place, we are looking into a few more complex
problems. The first are issues dealing with GDPR and privacy. While all our
pictures are takes in publically accessible locations, certain information on
them is considered sesnsitive data. This is mainly the case when license plate
numbers or people's faces are visible. While we do have manual procedures in
place to check for these things, they are time consuming and require a lot of
energy. So we are now looking into automatic recognition and possibly
automatic blurring of license plate numbers and faces using the 
`OpenCV <https://opencv.org/>`_ library. So far we have had very
good results with the license plates, but more mixed results with the
faces. We attribute this to the license plate formats being rather simple and
predictable. With the facial recognition, the main problem we are facing might
be more problematic in our line of work. The automated detection of faces is a
bit too eager and has a tendency to detect works of art like paintings,
sculptures or billboard as faces as well. Further work will be needed to
finetune this enough to make it fit for large-scale use.

.. image:: ilucidare_plate_censor.jpg

*The license plate on the left was automatically blurred with OpenCV*

Another avenue we are pursuing is automated detection of duplicate pictures. As
is often the case in large organisations, files are often distributed, copied and
mailed. Images are no exception to this rule. So, an image ends up being
present in different locations. All these duplicates cost storage space, which
can be expensive. Since every image also requires metadata, this also leads to
a duplication of metadata and the effort of creating it. So, we are now looking
into ways of automatically detecting duplicate images. So far, the technique of
`image hashing <https://www.pyimagesearch.com/2017/11/27/image-hashing-opencv-python/>`_ 
has proven to be very interesting and we will probably settle on a dHash algorithm.
Currently we are investigating how to properly integrate this in our image
archiving workflows so our colleagues gain all the benefits of this technique
without being confronted with the technical details too much. One could argue
that innovation only becomes productive when it goes hand in hand with
useability.

As a government agency dealing with immovable cultural heritage, almost all
data we collect have some spatial component. Our images are no different.
Almost every picture we take, is a picture of some kind of immovable cultural
heritage, be it an archaeological sites, a cultural landscape, a building, a
cemetary or another form of heritage. So we made a substantial effort to geolocate
the images in our image database. For older images, we did this by linking them
to the `heritage objects <https://inventaris.onroerenderfgoed.be/erfgoedobjecten_info>`_ 
they depict and copying their location. For newer images, we are relying on the
automated geolocation present in modern day smartphones and digital cameras.
The resulting GIS layer consists of point locations of most of our images and
can easily be visualised on our geoportal. For every picture you can then click
through to the image database to find out more about it, download it and reuse
it - provided you adhere to the license.

.. image:: ilucidare_geoportal_images.png

*A view of the Bijloke site in Ghent with all know images of this area.*

Give me a map and I'll never get lost
-------------------------------------

As we have stated, almost everything we do has a spatial component. For us,
maps are essential. Today, that means :ref:`category-GIS` is essential to us.
As a government agency we publish INSPIRE compliant datasets that get
distributed through the INSPIRE network across Europe. This is mostly aimed at
the professional GIS user, using his or her own desktop software. But we always
felt that we were lacking a certain part of our target audience. People wanting
to quickly find out what information we had for their neighbourhoods or 
properties. To this end, we created our own `Geoportal
<https://geo.onroerenderfgoed.be>`_, a simple web portal where a user can
consult a (hopefully) intuitive map of Flanders and see what kind of heritage
is present. We purposefullly built this portal for regular, non-GIS users. We
wanted it to feel like `Google Maps for Heritage`. While it's no longer a new
tool, it's still very popular among our users and gets used a lot on a daily
basis. Because we focus on presenting our own data as best as possible, the
interface is very optimised for people looking for spatial information on
heritage, as opposed to just any spatial data. Those people we gladly refer to
`Geopunt <https://geopunt.be>`_, a geoportal for all spatial data
produced by the Flemish Government. It contains far more data than we ever care
about, but it's use is not optimised for heritage information.

.. image:: ilucidare_geoportal_sotteghem.png

*The current day city of Zottegem and it's listed heritage as seen on the Villaret map (1745-1748)*

If you visit the geoportal for the first time, you will be asked to choose one
of two profiles. There are preset combinations of map layers. One shows a good
default selection for most people, the other one offers a combinations
optimised for users mostly interested in information that has legal
ramifications. This is mostly used by actuaries, real-estate agents, property
developers, other governments, ... If you're not satisfied by the default map
layers loaded, you can always load other information layers or base layers.
Some of these provide you with links to our other systems, such as the image
database we mentioned before or datasets of archaeological report that are
submitted by archaeologists and published by us. Among the base layers are
several different orthofotographic layers, but also historical maps. In our
portal users can consult maps dating as far back as the 18th and 19th
centuries. Some of these were provided by `Information Flanders`. Others, like
the `Villaret map (1745-1748) <https://www.onroerenderfgoed.be/nieuws/oudste-kaart-van-belgie-als-gratis-open-data>`_ 
were digitised by ourselves in cooperation with them. 

Have a look at `our portal <https://geo.onroerenderfgoed.be>`_ and browse the
map. Look at places you've seen, read more about them and their history and
browse the pictures we've collected!

When points become clouds of information
----------------------------------------

.. image:: ilucidare_geoportal_damme.png

*The city of Damme and it's fortifications as seen on the multidirectional
hillshade*

To wrap up, we present a final mapping related project. A while back, our
colleagues at `Flanders Information Agency <https://informatie.vlaanderen.be>`_
created a dataset called `Digitaal Hoogtemodel Vlaanderen (DHMV)
<https://overheid.vlaanderen.be/informatie-vlaanderen/producten-diensten/digitaal-hoogtemodel-dhmv>`_. This set of
LIDAR data consist of a Digital Surface Model (DSM) and a Digital Terrain Model 
(DTM). Together these datasets provide height related data and allow us to
visualise the terrain in Flanders in different ways. While the raw data is
available as open data, it takes quite a bit of knowledge and expertise to
visualise this data in a useful way. Therefor, a few standard renderings as
regular WMS maps have been available for a while. While interesting, we knew it
was posible to create `other visualisations better suited for archaeologists
<https://oar.onroerenderfgoed.be/item/452>`_.
These would allow easier detection of archaeological sites, based on
micro-topology. To this end, Flanders Heritage and Flanders Information
collaborated to create `two new renderings of the DHMV
<https://www.onroerenderfgoed.be/blog/vlaanderen-onder-de-scanner-twee-hoge-resolutie-verwerkingen-van-het-dhm-vlaanderen-ii-online>`_ 
and publish them. Each rendering uses different techniques and parameters. Depending 
on the kind of features you are looking for, one will suit you better than the other.

.. image:: ilucidare_geoportal_trenches.png

*Trenches and a fortress near Kapellen as seen on the skyview factor*

The final result has proven to be insightful and very useful to archaeologists
in their day to day job. By glancing at these two layers, either at our
geoportal or through a WMS service, they can quickly judge potential features
of a site they are researching. If you want to see it in action, head over to
the `geoportal <https://geo.onroerenderfgoed.be>`_ and select them under `Lagen
> Achtergrondlagen > Digitaal Hoogtemodel > DHMV II, multidirectionele
hillshare or DHMV II, skyview factor`. We have received some recognition for
the general usefulness of this product in the form of nominations for a
`Datanews ICT Project of the Year <https://datanewscio.be>`_ and an `Agoria
e-Gov Award Open Data
<https://www.agoria.be/nl/Agoria-e-Gov-Awards-2019-And-the-nominees-are>`_.

We hope that we have proven that there is a strong synergy between heritage in
technology as we make our way into the 21st century. As every organisation out
there, technology has become more and more ingrained in our day to day
operations. As Satya Nadella, the CEO of Microsoft, recently said: `Every
company is now a software company`. The same holds true for a government agency
or a cultural heritage institution. Software is everywhere. Digital is
everywhere. And even though our cultural heritage is still largely an analog
product, the information sources and tools we use to study it, no longer are
and never again will be.

If you have further questions, feel free to `contact us
<ict@onroerenderfgoed.be>`_, check out the rest of this blog, have a look at
our `open source projects <https://github.com/onroerendErfgoed>`_ or `website
<https://www.onroerenderfgoed.be>`_.
