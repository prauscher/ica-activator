#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

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
    def __init__(self):
        pass

    def auth(self, user, password):
        return random.choice([True, False])

    def search(self, user, password, string):
        return [
            {"memberId": 325, "name": "Philipp Metzler"},
            {"memberId": 523, "name": "Random Dude"},
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
        }

    def activate(self, user, password, memberId):
        return True
