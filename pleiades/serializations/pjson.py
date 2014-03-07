#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

"""
bbox list of floats
connectsWith (list of strings (IDs))
#description (string)
features (list of dictionaries, complex)
#id (string)
names (list of strings)
recent_changes (list of dictionaries)
reprPoint (list of numbers (2))
#title (string)
type string = FeatureCollection
"""

class PJSON():

    def __init__(self, data):
        self.json = json.dumps(data, sort_keys=True)
        return self.json


class PLACEJSON(PJSON):

    def __init__(self, data):
        d = {}

        # original Pleiades JSON keys
        d['type'] = 'FeatureCollection'
        d['reprPoint'] = [float(data['reprLong']),float(data['reprLat'])]
        d['connectsWith'] = data['hasConnectionsWith']
        d['bbox'] = [float(v.strip()) for v in data['bbox'].split(',')]
        orig = [
            'connectsWith',
            'description',
            'id',
            'title'
            ]
        for o in orig:
            try:
                d[o] = data[o]
            except:
                print ("csv doesn't contain '%s'" % o)
        # original CSV content not presently available in CSV dumps:
        # recent_changes
        # features (locations)
        # names

        # new Pleiades JSON keys
        new = [
            ['authors', "%s", 'authors'],
            ['created', "%s", 'created'],
            ['creators', "%s", 'creators'],
            ['currentVersion', "%s", 'currentVersion'],
            ['extent', "%s", 'extent'],
            ['featureTypes', "%s", 'featureTypes'],
            ['geoContext', "%s", 'geoContext'],
            ['locationPrecision', "%s", 'locationPrecision'],
            ['maxDate', "%s", 'maxDate'],
            ['minDate', "%s", 'minDate'],
            ['modified', "%s", 'modified'],
            ['placeuri', "http://pleiades.stoa.org/places/%s#this", 'id'],
            ['documenturi', "http://pleiades.stoa.org/places/%s", 'id'],
            ['tags', "%s", 'tags']
        ]
        for n in new:
            d[n[0]] =  n[1] % data[n[2]]

        PJSON.__init__(self, d)




