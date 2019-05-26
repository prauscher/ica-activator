#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import string
import random
import os.path
import os
from handlers.image import handleImage
from handlers.pdf import handlePdf

HANDLERS = {
    "jpg": handleImage,
    "jpeg": handleImage,
    "png": handleImage,
    "pdf": handlePdf,
}

CHARACTERS = string.ascii_lowercase


class FileStorage:
    def __init__(self, temporaryFolder, destinationFolder):
        self.temporaryFolder = temporaryFolder
        self.destinationFolder = destinationFolder

    def _getTemporaryFilepath(self, username, fileId):
        return os.path.join(
            self.temporaryFolder,
            username + "-" + fileId + ".jpg")

    def _generateTemporaryFilename(self, username):
        while True:
            fileId = "".join(random.choice(CHARACTERS) for i in range(10))
            filePath = self._getTemporaryFilepath(username, fileId)
            if not os.path.isfile(filePath):
                return fileId, filePath

    def _getPermanentFilepath(self, memberId):
        return os.path.join(self.destinationFolder, memberId + ".jpg")

    def storeFileTemporary(self, username, file):
        extension = file.filename.split(".")[-1][0:7]
        if extension not in HANDLERS:
            raise Exception("Extension {} is not allowed".format(extension))
        handler = HANDLERS[extension]

        fileId, filePath = self._generateTemporaryFilename(username)

        with open(filePath, "wb") as fp:
            fp.write(handler(file.value))

        return fileId

    def getPreview(self, username, fileId):
        filePath = self._getTemporaryFilepath(username, fileId)
        with open(filePath, "rb") as fb:
            data = fb.read()
        return data

    def storeFile(self, username, fileId, memberId):
        destination = self._getPermanentFilepath(memberId)

        if os.path.exists(destination):
            raise StorageException(
                "Es existiert bereits ein Antrag für Mitglied " + memberId)

        os.rename(
            self._getTemporaryFilepath(username, fileId),
            self._getPermanentFilepath(memberId))


class UploadException(Exception):
    pass


class StorageException(Exception):
    pass
