#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

class PJSON():
    """
    basic JSON output class for Pleiades JSON
    """

    def __init__(self, data):
        """
        convert dictionary to json string with sorted keys
        """
        self.json = json.dumps(data, sort_keys=True)


class PLACEJSON(PJSON):
    """
    JSON output class for Pleiades places
    """

    def __init__(self, placedata, namedata=None, locationdata=None):
        """
        create json from placedata object and optional name and location data objects
        """

        # construct a dictionary from which to serialize the JSON
        d = {}

        # legacy Pleiades JSON fields: don't change these becaue third parties expect them just so
        orig = [
            'connectsWith',
            'description',
            'id',
            'title'
        ]
        for o in orig:
            d[o] = placedata[o]
        d['type'] = 'FeatureCollection'
        d['reprPoint'] = [float(placedata['reprLong']),float(placedata['reprLat'])]
        d['connectsWith'] = placedata['hasConnectionsWith']
        d['bbox'] = [float(v.strip()) for v in placedata['bbox'].split(',')]
        pid = placedata['id']
        if namedata:
            try:
                nn = namedata.pidx[pid]
            except KeyError:
                pass
            else:
                names = []
                toponyms = []  # structured toponyms are a new component of Pleiades Place JSON
                for i in nn:
                    n = namedata.data[i]['nameAttested'].strip()
                    topod = {}
                    if n != "":
                        names.append(n)
                        topod['nameAttested'] = n
                    t = namedata.data[i]['nameTransliterated']
                    names.extend([n.strip() for n in t.split(',') if n.strip() != ""])
                    if t.strip() != "":
                        topod['nameTransliterated'] = t.strip()
                    try:
                        topod['nameLanguage'] = namedata.data[i]['nameLanguage'] 
                    except KeyError:
                        pass
                    minDate = int(float(namedata.data[i]['minDate']))
                    maxDate = int(float(namedata.data[i]['maxDate']))
                    topod['minDate'] = "%s" % minDate
                    topod['maxDate'] = "%s" % maxDate
                    topod['dateRange'] = "%s - %s" % (str(["AD %s" % minDate, "%s BC" % str(minDate*(-1))][minDate < 0]), str(["AD %s" % maxDate, "%s BC" % str(maxDate*(-1))][maxDate < 0]))
                    toponyms.append(topod)
                d['names'] = sorted(list(set(names)))
                d['toponyms'] = toponyms
        if locationdata:
            try:
                ll = locationdata.pidx[pid]
            except KeyError:
                pass
            else:
                features = []
                for i in ll:
                    l = {}
                    l['geometry'] = locationdata.data[i]['geometry']
                    l['type'] = 'Feature'
                    minDate = int(float(locationdata.data[i]['minDate']))
                    maxDate = int(float(locationdata.data[i]['maxDate']))
                    dateRange = "%s - %s" % (str(["AD %s" % minDate, "%s BC" % str(minDate*(-1))][minDate < 0]), str(["AD %s" % maxDate, "%s BC" % str(maxDate*(-1))][maxDate < 0]))
                    l['properties'] = {
                        'snippet': "%s; %s" % (locationdata.data[i]['featureTypes'], dateRange),
                        'link': "http://pleiades.stoa.org/places/%s/%s" % (pid, locationdata.data[i]['id']),
                        'description':locationdata.data[i]['description'],
                        'location_precision':locationdata.data[i]['locationPrecision'],
                        'title': locationdata.data[i]['title'],
                        'minDate': "%s" % minDate,  # new field
                        'maxDate': "%s" % maxDate,  # new field
                        'dateRange': "%s" % dateRange  #new field
                    }
                    l['id'] = locationdata.data[i]['id']
                    features.append(l)
                d['features'] = features

        # CSV data that is in the nightly dumps, so we can add to Pleiades JSON
            # NB, we calculate and add toponyms above because it's more efficient
        new = [
            ['authors', "%s", 'authors'],
            ['created', "%s", 'created'],
            ['creators', "%s", 'creators'],
            ['currentVersion', "%s", 'currentVersion'],
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
            d[n[0]] =  n[1] % placedata[n[2]]
        d['extent'] = placedata['extent']

        # desireable content not presently available in CSV dumps, so not currently in output
            # recent_changes
            # horizontal accuracy
            # provenance
            # license
            # certainty measures
            # gather up authors from children and make them "contributors" if not in the place author string? 

        # parent class knows how to turn dictionary into JSON
        PJSON.__init__(self, d)




