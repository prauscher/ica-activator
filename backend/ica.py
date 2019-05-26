#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

import datetime
import random
import hmac

MEMBERSHIP_ORDINARY = 1
MEMBERSHIP_SECONDARY = 2
MEMBERSHIP_SUPPORTING = 3
MEMBERSHIP_JURISTIC = 4

GENDER_MALE = 369
GENDER_FEMALE = 370
GENDER_VARIOUS = 371

ALLOWED_HASHES = [
    "cb942e814af87e97e5be94c8fd7a3b2b",
    "8e19eeeb40d7e7ff92f054f099846650",
]


def _calculate_hash(username, password):
    return hmac.new(username.encode("utf-8"),
                    password.encode("utf-8")).hexdigest()


class IcaConnector:
    def __init__(self):
        pass

    def auth(self, user, password):
        return _calculate_hash(user, password) in ALLOWED_HASHES

    def search(self, user, password, string):
        return [
            {"memberId": random.randint(100, 199), "name": "Philipp Metzler"},
            {"memberId": random.randint(200, 299), "name": "Random Dude"},
        ]

    def get(self, user, password, id):
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

    def activate(self, user, password, memberId):
        return True


if __name__ == "__main__":
    import sys
    print(_calculate_hash(sys.argv[1], sys.argv[2]))
