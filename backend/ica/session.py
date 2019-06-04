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

    def search(self, string):
        # Sadly, ica does not allow for anytext-filters...
        # TODO implement caching
        filter = {"mglStatusId": "WARTEND"}
        resp = self._call("GET",
                          "rest/nami/search-multi/result-list",
                          params={"searchedValues": json.dumps(filter)})
        if not resp["success"]:
            raise IcaApiException(resp["message"])

        return [{"memberId": e["entries_id"], "name": e["descriptor"]}
                for e in resp["data"]
                if string in e["descriptor"]]

    def get(self, id):
        filter = {"mitgliedsNummer": id}
        resp = self._call("GET",
                          "rest/nami/search-multi/result-list",
                          params={"searchedValues": json.dumps(filter)})
        if not resp["success"]:
            raise IcaApiException(resp["message"])

        print(resp)
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
