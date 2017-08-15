#!/bin/bash

wget http://koditvepg.com/epg/uk.xml.gz

echo "Unzipping file"
gunzip uk.xml.gz

echo "Renaming files"
mv -f uk.xml EPG.xml
