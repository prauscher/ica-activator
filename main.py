#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tg import FullStackApplicationConfigurator
import socket
from controller import RootController
from wsgiref.simple_server import WSGIServer, make_server

config = FullStackApplicationConfigurator()
config.update_blueprint({
    'root_controller': RootController(),
    'renderers': ['jinja'],
    'use_dotted_templatenames': False,
    'serve_static': True,
    'paths': {
        'static_files': 'static',
    },
})


# fix for ipv6
class server_cls(WSGIServer):
    address_family = socket.AF_INET6


application = config.make_wsgi_app()
print("Serving on port 8080...")
httpd = make_server('::1', 8080, application, server_cls)
httpd.serve_forever()
