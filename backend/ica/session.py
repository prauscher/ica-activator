#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
from pprint import pformat
import datetime
import random

MEMBERSHIP_ORDINARY = 1
MEMBERSHIP_SECONDARY = 2
MEMBERSHIP_SUPPORTING = 3
MEMBERSHIP_JURISTIC = 4

GENDER_MALE = 369
GENDER_FEMALE = 370
GENDER_VARIOUS = 371


class IcaSession:
    sessionId = None

    def __init__(self, endpoint):
        if not endpoint.endswith("/"):
            endpoint = endpoint + "/"

        self.endpoint = endpoint

    def _call(self, method, path, **kwargs):
        url = self.endpoint + path
        cookies = {}
        if self.sessionId is not None:
            cookieName, cookieValue = self.sessionId
            cookies[cookieName] = cookieValue
        print("DEBUG: => {} {}".format(url, pformat(kwargs)))
        resp = requests.request(method, url, cookies=cookies, **kwargs).json()
        print("DEBUG: <= {}".format(pformat(resp)))
        return resp

    def auth(self, user, password):
        authData = {
            "username": user,
            "password": password,
            "Login": "API",
        }
        resp = self._call("POST",
                          "rest/nami/auth/manual/sessionStartup",
                          data={"username": user,
                                "password": password,
                                "Login": "API"})
        if resp["statusCode"] != 0:
            raise IcaApiException(resp["statusMessage"])
        self.sessionId = (resp["apiSessionName"], resp["apiSessionToken"])
        return True

    def search(self, filter):
        resp = self._call("GET",
                          "rest/nami/search-multi/result-list",
                          params={"searchedValues": json.dumps(filter)})
        if not resp["success"]:
            raise IcaApiException(resp["message"])

        print(resp["data"])
        return resp["data"]

    def get(self, gliederungId, memberId):
        resp = self._call("GET",
                          "rest/nami/mitglied/filtered-for-navigation/" \
                          "gruppierung/gruppierung/{}/{}" \
                          .format(int(gliederungId), int(memberId)))
        if not resp["success"]:
            raise IcaApiException(resp["message"])

        print(resp["data"])
        return resp["data"]

    def activate(self, id, reason=""):
        resp = self._call("POST",
                          "rest/mgl-aufnahme/genehmige/{}".format(int(id)),
                          json=[{"genehmigt": "true", "inhalt": reason}])
        if not resp["success"]:
            raise IcaApiException(resp["message"])


class IcaApiException(Exception):
    pass
