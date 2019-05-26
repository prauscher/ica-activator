#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tg import expose, redirect, session, TGController
from urllib.parse import quote


def get_userdata():
    return session["user"]

def require_login():
    def decorator(func):
        def wrapper(*args, **kwargs):
            if "user" not in session:
                redirect("/user/login.html")
            else:
                return func(*args, **kwargs)
        return wrapper
    return decorator


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

    @expose()
    def logout(self):
        del(session["user"])
        session.save()
        return "success"
