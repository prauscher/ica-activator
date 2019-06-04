#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

from .session import IcaSession
import datetime
import random

MEMBERSHIP_ORDINARY = 1
MEMBERSHIP_SECONDARY = 2
MEMBERSHIP_SUPPORTING = 3
MEMBERSHIP_JURISTIC = 4

GENDER_MALE = 369
GENDER_FEMALE = 370
GENDER_VARIOUS = 371


class IcaConnector:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def auth(self, user, password):
        session = IcaSession(self.endpoint)
        return session.auth(user, password)

    def search(self, user, password, string):
        session = IcaSession(self.endpoint)
        session.auth(user, password)
        return session.search(string)

    def get(self, user, password, id):
        session = IcaSession(self.endpoint)
        session.auth(user, password)
        return session.get(id)

    def activate(self, user, password, memberId):
        session = IcaSession(self.endpoint)
        session.auth(user, password)
        return session.activate(memberId)
