#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tg import FullStackApplicationConfigurator
import icaactivator

base_config = FullStackApplicationConfigurator()
base_config.update_blueprint({
    'package': icaactivator,
    'renderers': ['jinja', 'json'],
    'default_renderer': 'jinja',
    'use_dotted_templatenames': False,
    'session.enabled': True,
})
