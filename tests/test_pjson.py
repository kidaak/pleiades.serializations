#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pjson
----------------------------------

Tests for `pjson` module of the pleiades.serializations project.
"""

from nose.tools import *

from pleiades.serializations import pcsv, pjson


def test_placejson():
    pd = pcsv.PleiadesDump('tests/data/pleiades-places-latest.csv')
    p = pjson.PLACEJSON(pd.data[0])
    print p.json
    assert_equal(p.json, '{"description": "An ancient place, cited: BAtlas 27 B2 Consabura/Consabrum", "documenturi": "http://pleiades.stoa.org/places/265876", "id": "265876", "placeuri": "http://pleiades.stoa.org/places/265876#this", "title": "Consabura/Consabrum"}')
