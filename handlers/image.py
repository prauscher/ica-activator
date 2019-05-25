#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import io
from PIL import Image


def handleImage(data):
    inStream = io.BytesIO(data)
    image = Image.open(inStream)
    image.thumbnail((1000, 1000))
    image = image.convert("RGB")
    outStream = io.BytesIO()
    image.save(outStream, format="jpeg", dpi=(300, 300))
    return outStream.getvalue()
