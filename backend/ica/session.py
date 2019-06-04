#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
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

    def _call(self, method, data={}):
        url = self.endpoint + method
        cookies = {}
        if self.sessionId is not None:
            cookieName, cookieValue = self.sessionId
            cookies[cookieName] = cookieValue
        print("DEBUG: => {} {}".format(url, pformat(data)))
        resp = requests.post(url, data=data, cookies=cookies).json()
        print("DEBUG: <= {}".format(pformat(resp)))
        return resp

    def auth(self, user, password):
        authData = {
            "username": user,
            "password": password,
            "Login": "API",
        }
        resp = self._call("rest/nami/auth/manual/sessionStartup", authData)
        if resp["statusCode"] != 0:
            raise IcaApiException(resp["statusMessage"])
        self.sessionId = (resp["apiSessionName"], resp["apiSessionToken"])
        return True

    def search(self, string):
        return [
            {"memberId": random.randint(100, 199), "name": "Philipp Metzler"},
            {"memberId": random.randint(200, 299), "name": "Random Dude"},
        ]

    def get(self, id):
        return {
            "givenName": "Philipp",
            "surname": "Metzler",
            "gender": GENDER_MALE,
            "membership": MEMBERSHIP_ORDINARY,
            "additionalAddress": "",
            "street": "Mittwaldallee 7",
            "cityCode": "41561",
            "city": "Barnbeck",
            "birthDate": datetime.date(2003, 5, 7),
            "mail": "metzler@example.com",
            "mailGuardian": "eltern@example.org",
            "phoneNumber": "+49 123456",
            "mobileNumber": "+49 987654",
            "reason1": "-",
            "reason2": "-",
            "membershipDate": datetime.date(2019, 5, 24),
            "department": "Graue Bären",
        }

    def activate(self, id):
        return True


class IcaApiException(Exception):
    pass


if __name__ == "__main__":
    import sys
    print(_calculate_hash(sys.argv[1], sys.argv[2]))
