#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv

class PleiadesDump():

    def __init__(self, fn):
        with open(fn, 'rb') as csvfile:
            #dialect = csv.Sniffer().sniff(csvfile.read(1024))
            #csvfile.seek(0)
            reader = csv.reader(csvfile)
            self.rows = [row for row in reader]
            self.keys = sorted(self.rows[0])
            self.data = []
            for row in self.rows[1:]:
                d = dict(zip(self.keys, row))
                self.data.append(d)

    
