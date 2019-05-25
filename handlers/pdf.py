#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pdf2image import convert_from_bytes
import io


def handlePdf(data):
    images = convert_from_bytes(data, dpi=120, first_page=0, last_page=0)
    image = images[0]
    image.thumbnail((1000, 1000))
    image = image.convert("RGB")
    outStream = io.BytesIO()
    image.save(outStream, format="jpeg", dpi=(120, 120))
    return outStream.getvalue()
