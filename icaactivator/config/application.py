#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .app_cfg import base_config


def make_app(global_conf, **app_conf):
    app = base_config.make_wsgi_app(global_conf, app_conf, wrap_app=None)
    return app
