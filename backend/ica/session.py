#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hmac
import datetime
import random

ALLOWED_HASHES = [
    "cb942e814af87e97e5be94c8fd7a3b2b",
    "8e19eeeb40d7e7ff92f054f099846650",
]

MEMBERSHIP_ORDINARY = 1
MEMBERSHIP_SECONDARY = 2
MEMBERSHIP_SUPPORTING = 3
MEMBERSHIP_JURISTIC = 4

GENDER_MALE = 369
GENDER_FEMALE = 370
GENDER_VARIOUS = 371


def _calculate_hash(username, password):
    return hmac.new(username.encode("utf-8"),
                    password.encode("utf-8")).hexdigest()


class IcaSession:
    session_id = None

    def __init__(self, endpoint):
        if not endpoint.endswith("/"):
            endpoint = endpoint + "/"

        self.endpoint = endpoint

    def auth(self, user, password):
        self.session_id = "AAA"
        return _calculate_hash(user, password) in ALLOWED_HASHES

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
