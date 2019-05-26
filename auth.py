#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tg import expose, redirect, session, TGController
from tg.decorators import before_validate
from urllib.parse import quote


def get_userdata():
    return session["user"]


class require_login(before_validate):
    def __init__(self):
        super(require_login, self).__init__(self.check_auth)

    def check_auth(self, remainder, params):
        if "user" not in session:
            redirect("/user/login.html")


class UserController(TGController):
    def __init__(self, userChecker, redirectTarget):
        self.userChecker = userChecker
        self.redirectTarget = redirectTarget

    @expose("templates/login.xhtml")
    def login(self, username=None, password=None):
        if username is None or password is None:
            # render form
            return {}

        if self.userChecker(username, password):
            session["user"] = {"username": username, "password": password}
            session.save()
            redirect(self.redirectTarget)
        else:
            return {"success": False}

    @expose("json")
    def logout(self):
        del(session["user"])
        session.save()
        return {"success": True}
