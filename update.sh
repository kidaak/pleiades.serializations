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
cd $3
rm -rf *
cd $1

source ~/Envs/pleiades-serializations/bin/activate
python gen_json.py $2 $3

