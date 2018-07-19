#!/usr/bin/env bash

source bin/activate
echo '' > result.json
scrapy runspider spider.py -o result.json 
./jsonToMd.py > packages.md