#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

import datetime

MEMBERSHIP_ORDINARY = 1
MEMBERSHIP_SECONDARY = 2
MEMBERSHIP_SUPPORTING = 3
MEMBERSHIP_JURISTIC = 4

GENDER_MALE = 1
GENDER_FEMALE = 2
GENDER_VARIOUS = 3


class IcaConnector:
    def __init__(self):
        pass

    def auth(self, user, password):
        # return False
        return True

    def search(self, string):
        return [
            {"memberId": 325, "name": "Philipp Metzler"},
            {"memberId": 523, "name": "Random Dude"},
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
            "reason1": "-",
            "reason2": "-",
        }

    def activate(self, memberId):
        return True
