#!/bin/bash
set -x

origdir=$(pwd)
cd $1
rm *.gz
rm *.csv
curl -O http://atlantides.org/downloads/pleiades/dumps/pleiades-locations-latest.csv.gz
curl -O http://atlantides.org/downloads/pleiades/dumps/pleiades-names-latest.csv.gz
curl -O http://atlantides.org/downloads/pleiades/dumps/pleiades-places-latest.csv.gz
gzip -d pleiades-locations-latest.csv.gz 
gzip -d pleiades-names-latest.csv.gz 
gzip -d pleiades-places-latest.csv.gz 
cd $origdir
cd $2
rm -rf *
cd $origdir
source ~/Envs/pleiades-serializations/bin/activate
python gen_json.py $1 $2

