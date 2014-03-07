#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_csv
----------------------------------

Tests for `csv` module of the pleiades.serializations project.
"""

from nose.tools import *

from pleiades.serializations import pcsv

def test_places_load():
    pd = pcsv.PleiadesDump('tests/data/pleiades-places-latest.csv')
    assert_equal(pd.keys, ['authors','bbox','connectsWith','created','creators','currentVersion','description','extent','featureTypes','geoContext','hasConnectionsWith','id','locationPrecision','maxDate','minDate','modified','path','reprLat','reprLatLong','reprLong','tags','timePeriods','timePeriodsKeys','timePeriodsRange','title','uid'])
    assert_equal(len(pd.rows), 34689)
    assert_equal(sorted(pd.data[0].keys()), pd.keys)

def test_names_load():
    pd = pcsv.PleiadesDump('tests/data/pleiades-names-latest.csv')
    assert_equal(pd.keys, ['authors','avgRating', 'bbox','created','creators','currentVersion','description','extent','id','locationPrecision','maxDate','minDate','modified','nameAttested', 'nameLanguage', 'nameTransliterated', 'numRatings', 'path','pid', 'reprLat','reprLatLong','reprLong','tags','timePeriods','timePeriodsKeys','timePeriodsRange','title','uid'])
    assert_equal(len(pd.rows), 30071)
    assert_equal(sorted(pd.data[0].keys()), pd.keys)

def test_locations_load():
    pd = pcsv.PleiadesDump('tests/data/pleiades-locations-latest.csv')
    assert_equal(pd.keys, ['authors', 'avgRating', 'bbox','created','creators','currentVersion','description','featureTypes','geometry', 'id','locationPrecision','maxDate','minDate','modified','numRatings', 'path','pid','reprLat','reprLatLong','reprLong','tags','timePeriods','timePeriodsKeys','timePeriodsRange','title','uid'])
    assert_equal(len(pd.rows), 38635)
    assert_equal(sorted(pd.data[0].keys()), pd.keys)




