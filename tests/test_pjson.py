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
    pd = pcsv.PleiadesDump('tests/data/consabura-places.csv')
    p = pjson.PLACEJSON(pd.data[0])
    assert_equal(p.json, '{"authors": "Spann, P., DARMC, R. Talbert, R. Warner, S. Gillies, T. Elliott", "bbox": [-3.606772, 39.460299, -3.606772, 39.460299], "connectsWith": "", "created": "2010-09-24T19:02:22Z", "creators": "P.O. Spann", "currentVersion": "12", "description": "An ancient place, cited: BAtlas 27 B2 Consabura/Consabrum", "documenturi": "http://pleiades.stoa.org/places/265876", "extent": {"coordinates": [-3.606772, 39.460299], "type": "Point"}, "featureTypes": "settlement", "geoContext": "Consuegra", "id": "265876", "locationPrecision": "precise", "maxDate": "640.0", "minDate": "-330.0", "modified": "2012-10-23T15:29:53Z", "placeuri": "http://pleiades.stoa.org/places/265876#this", "reprPoint": [-3.606772, 39.460299], "tags": "dare:ancient=1, dare:major=1, dare:feature=major settlement", "title": "Consabura/Consabrum", "type": "FeatureCollection"}')

def test_placejsonwithnames():
    pd = pcsv.PleiadesDump('tests/data/consabura-places.csv')
    nd = pcsv.PleiadesDump('tests/data/consabura-names.csv')
    p = pjson.PLACEJSON(pd.data[0], nd)
    assert_equal(p.json, '{"authors": "Spann, P., DARMC, R. Talbert, R. Warner, S. Gillies, T. Elliott", "bbox": [-3.606772, 39.460299, -3.606772, 39.460299], "connectsWith": "", "created": "2010-09-24T19:02:22Z", "creators": "P.O. Spann", "currentVersion": "12", "description": "An ancient place, cited: BAtlas 27 B2 Consabura/Consabrum", "documenturi": "http://pleiades.stoa.org/places/265876", "extent": {"coordinates": [-3.606772, 39.460299], "type": "Point"}, "featureTypes": "settlement", "geoContext": "Consuegra", "id": "265876", "locationPrecision": "precise", "maxDate": "640.0", "minDate": "-330.0", "modified": "2012-10-23T15:29:53Z", "names": ["Consabrum", "Consabura", "Kondabora"], "placeuri": "http://pleiades.stoa.org/places/265876#this", "reprPoint": [-3.606772, 39.460299], "tags": "dare:ancient=1, dare:major=1, dare:feature=major settlement", "title": "Consabura/Consabrum", "toponyms": [{"dateRange": "330 BC - AD 640", "maxDate": "640", "minDate": "-330", "nameLanguage": "", "nameTransliterated": "Consabura"}, {"dateRange": "330 BC - AD 640", "maxDate": "640", "minDate": "-330", "nameLanguage": "", "nameTransliterated": "Consabrum"}, {"dateRange": "330 BC - AD 640", "maxDate": "640", "minDate": "-330", "nameLanguage": "", "nameTransliterated": "Kondabora"}], "type": "FeatureCollection"}')

def test_placejsonwithfeatures():
    pd = pcsv.PleiadesDump('tests/data/consabura-places.csv')
    ld = pcsv.PleiadesDump('tests/data/consabura-locations.csv')
    p = pjson.PLACEJSON(pd.data[0], locationdata=ld)
    assert_equal(p.json, '{"authors": "Spann, P., DARMC, R. Talbert, R. Warner, S. Gillies, T. Elliott", "bbox": [-3.606772, 39.460299, -3.606772, 39.460299], "connectsWith": "", "created": "2010-09-24T19:02:22Z", "creators": "P.O. Spann", "currentVersion": "12", "description": "An ancient place, cited: BAtlas 27 B2 Consabura/Consabrum", "documenturi": "http://pleiades.stoa.org/places/265876", "extent": {"coordinates": [-3.606772, 39.460299], "type": "Point"}, "featureTypes": "settlement", "features": [{"geometry": {"coordinates": [-3.606772, 39.460299], "type": "Point"}, "id": "darmc-location-20192", "properties": {"dateRange": "330 BC - AD 640", "description": "1M scale point location", "link": "http://pleiades.stoa.org/places/265876/darmc-location-20192", "location_precision": "precise", "maxDate": "640", "minDate": "-330", "snippet": "unknown; 330 BC - AD 640", "title": "DARMC location 20192"}, "type": "Feature"}], "geoContext": "Consuegra", "id": "265876", "locationPrecision": "precise", "maxDate": "640.0", "minDate": "-330.0", "modified": "2012-10-23T15:29:53Z", "placeuri": "http://pleiades.stoa.org/places/265876#this", "reprPoint": [-3.606772, 39.460299], "tags": "dare:ancient=1, dare:major=1, dare:feature=major settlement", "title": "Consabura/Consabrum", "type": "FeatureCollection"}')

def test_placejsonwrite():
    pd = pcsv.PleiadesDump('tests/data/consabura-places.csv')
    nd = pcsv.PleiadesDump('tests/data/consabura-names.csv')
    ld = pcsv.PleiadesDump('tests/data/consabura-locations.csv')
    p = pjson.PLACEJSON(pd.data[0], nd, ld)
    p.write('tests/output')

def test_placejsonmultiwrite():
    pd = pcsv.PleiadesDump('tests/data/multi-places.csv')
    nd = pcsv.PleiadesDump('tests/data/multi-names.csv')
    ld = pcsv.PleiadesDump('tests/data/multi-locations.csv')
    for datum in pd.data:
        p = pjson.PLACEJSON(datum, nd, ld)
        p.write('tests/output')


