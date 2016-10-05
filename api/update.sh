#!/bin/bash

TOKEN=$APIDOCSTOKEN

# curl -vH "Authorization: token $TOKEN" -o besluiten/api.rst https://raw.githubusercontent.com/OnroerendErfgoed/besluiten/0.8.1/docs/service.rst
curl -vH "Authorization: token $TOKEN" -o geozoekdiensten/api.rst https://raw.githubusercontent.com/OnroerendErfgoed/geozoekdiensten/0.3.1/docs/services.rst
