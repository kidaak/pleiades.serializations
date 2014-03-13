#!/bin/bash
set -x

cd $2
rm *.gz
rm *.csv
curl -O http://atlantides.org/downloads/pleiades/dumps/pleiades-locations-latest.csv.gz
curl -O http://atlantides.org/downloads/pleiades/dumps/pleiades-names-latest.csv.gz
curl -O http://atlantides.org/downloads/pleiades/dumps/pleiades-places-latest.csv.gz
gzip -d pleiades-locations-latest.csv.gz 
gzip -d pleiades-names-latest.csv.gz 
gzip -d pleiades-places-latest.csv.gz 
cd $1

source ~/Envs/pleiades-serializations/bin/activate
python gen_json.py -v $2 $3

