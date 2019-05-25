#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tg import expose, redirect, TGController
from tg.controllers.util import abort
from auth import UserController, require_login
from backend.ica import IcaConnector
from backend.files import FileStorage

ica = IcaConnector()
fileStorage = FileStorage("./temp", "./storage")


class RootController(TGController):
    user = UserController(userChecker=ica.auth, redirectTarget="/search.html")

    @expose()
    def index(self):
        redirect("/search.html")

    @expose("templates/search.xhtml")
    @require_login()
    def search(self):
        return {}

    @expose()
    @require_login()
    def upload(self, applicationFile):
        fileId = fileStorage.storeFileTemporary(applicationFile)
        redirect("/review.html?fileId={}".format(fileId))

    @expose("templates/review.xhtml")
    @require_login()
    def review(self, fileId):
        return {"fileId": fileId}

    @expose(content_type="image/jpg")
    @require_login()
    def application(self, id):
        try:
            return fileStorage.getPreview(id)
        except FileNotFoundError:
            abort(404)

    @expose("json")
    @require_login()
    def activate(self, fileId, memberId):
        try:
            fileStorage.storeFile(fileId, memberId)
            ica.activate(memberId)
            return {"success": True}
        except:
            return {"success": False}

    @expose("json")
    @require_login()
    def find(self, query):
        return {"data": ica.search(query)}

    @expose("json")
    @require_login()
    def query(self, memberId):
        return {"data": ica.get(memberId)}
