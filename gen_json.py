#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Generate Pleiades JSON
"""

import argparse
import os
import sys
import traceback
import logging as l

from pleiades.serializations import pcsv, pjson

SCRIPT_DESC = 'Generates new-fangled Pleiades JSON from Pleiades CSV dumps'

def main ():

    global args

    if args.verbose:
        l.basicConfig(level=l.DEBUG)
    else:
        l.basicConfig(level=l.WARNING)
    datadir = args.datadir
    outdir = args.outdir

    datadir = os.path.abspath(datadir)
    if not os.path.isdir(datadir):
        raise IOError('data input directory not found at "%s"' % datadir)
    l.debug('input data will be read from "%s"' % datadir)

    outdir = os.path.abspath(outdir)
    if not os.path.isdir(outdir):
        raise IOError('csv output directory not found at "%s"' % outdir)
    l.debug('output data will be written in "%s"' % outdir)

    dataparts = datadir.split('/')

    l.debug('>>> loading places data...')
    pd = pcsv.PleiadesDump(os.path.join(datadir,'pleiades-places-latest.csv'))
    l.debug('>>> loading names data...')
    nd = pcsv.PleiadesDump(os.path.join(datadir,'pleiades-names-latest.csv'))
    l.debug('>>> loading locations data...')
    ld = pcsv.PleiadesDump(os.path.join(datadir,'pleiades-locations-latest.csv'))
    l.debug('>>> trying to write output...')
    for datum in pd.data:
        p = pjson.PLACEJSON(datum, nd, ld)
        l.debug('place id: %s' % p.id)
        p.write(outdir)





if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description=SCRIPT_DESC, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        parser.add_argument ("-v", "--verbose", action="store_true", default=False, help="verbose output")
        parser.add_argument ("datadir", help="data directory from which CSV will be read")
        parser.add_argument ("outdir", help="output directory wherein the output hierarchy will be constructed")
        args = parser.parse_args()
        main()
        sys.exit(0)
    except KeyboardInterrupt, e: # Ctrl-C
        raise e
    except SystemExit, e: # sys.exit()
        raise e
    except Exception, e:
        print "ERROR, UNEXPECTED EXCEPTION"
        print str(e)
        traceback.print_exc()
        os._exit(1)
