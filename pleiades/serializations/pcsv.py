#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import cStringIO
import csv
import json
import logging
import re



rex = re.compile('\\"')

class UTF8Recoder:
    def __init__(self, f, encoding):
        self.reader = codecs.getreader(encoding)(f)
    def __iter__(self):
        return self
    def next(self):
        return self.reader.next().encode("utf-8")

class UnicodeReader:
    def __init__(self, f, dialect=csv.excel, encoding="utf-8-sig", **kwds):
        f = UTF8Recoder(f, encoding)
        self.reader = csv.reader(f, dialect=dialect, **kwds)
    def next(self):
        row = self.reader.next()
        return [unicode(s, "utf-8") for s in row]
    def __iter__(self):
        return self

class UnicodeWriter:
    def __init__(self, f, dialect=csv.excel, encoding="utf-8-sig", **kwds):
        self.queue = cStringIO.StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()
    def writerow(self, row):
        self.writer.writerow([s.encode("utf-8") for s in row])
        data = self.queue.getvalue()
        data = data.decode("utf-8")
        data = self.encoder.encode(data)
        self.stream.write(data)
        self.queue.truncate(0)


class PleiadesDump():
    """
    read a Pleiades CSV dump file and parse it into an object that makes data access easy (i.e., by entity and with id indexes)
    """
    def __init__(self, fn):
        with open(fn, 'rb') as csvfile:
            reader = UnicodeReader(csvfile, encoding='utf-8')
            # store raw rows
            logging.debug('storing raw rows')
            self.rows = [row for row in reader]
            # make easy access to keys
            logging.debug('grabbing data keys')
            self.keys = sorted(self.rows[0])
            # parse data out of rows and into a list of dictionaries
            logging.debug('parsing data rows into list of dicts')
            self.data = []
            for row in self.rows[1:]:
                d = dict(zip(self.keys, row))
                try:
                    extent = d['extent']
                except KeyError:
                    pass
                else:
                    extent = rex.sub('"', extent)
                    d['extent'] = json.loads(extent)
                try:
                    geometry = d['geometry']
                except KeyError:
                    pass
                else:
                    geometry = rex.sub('"', geometry)
                    d['geometry'] = json.loads(geometry)
                self.data.append(d)
            # if CSV contains a "pid" field, create a pid-based index into self.data
            try:
                pid = self.data[0]['pid']
            except KeyError:
                pass
            else:
                logging.debug('creating pid index')
                self.pidx = {}
                for i,d in enumerate(self.data):
                    pid = d['pid']
                    if pid in self.pidx.keys():
                        self.pidx[pid].append(i)
                    else:
                        self.pidx[pid] = [i,]

    
