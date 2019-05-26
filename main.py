#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tg import FullStackApplicationConfigurator
from controller import RootController
from wsgiref.simple_server import make_server

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

application = config.make_wsgi_app()
print("Serving on port 8080...")
httpd = make_server('::1', 8080, application)
httpd.serve_forever()
