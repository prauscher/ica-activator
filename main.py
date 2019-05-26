#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tg import FullStackApplicationConfigurator
import socket
from icaactivator.config.app_cfg import base_config
from wsgiref.simple_server import WSGIServer, make_server


# fix for ipv6
class server_cls(WSGIServer):
    address_family = socket.AF_INET6


application = base_config.make_wsgi_app()
print("Serving on port 8080...")
httpd = make_server('::1', 8080, application, server_cls)
httpd.serve_forever()
