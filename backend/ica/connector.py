#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

from .session import IcaSession, IcaApiException


class IcaConnector:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def auth(self, user, password):
        session = IcaSession(self.endpoint)
        try:
            return session.auth(user, password)
        except IcaApiException:
            return False

    def getWaiting(self, user, password):
        session = IcaSession(self.endpoint)
        session.auth(user, password)
        return session.search({"mglStatusId": "WARTEND"})

    def activate(self, user, password, memberId):
        session = IcaSession(self.endpoint)
        session.auth(user, password)
        return session.activate(memberId)
