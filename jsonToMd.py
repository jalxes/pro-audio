#!/usr/bin/env python
import json

json_data = open('result.json').read()

data = json.loads(json_data)

print('|original link|name|description|')
print('|---|---|---|')
for x in data:
    print('|[ArchLink](%s)|[%s](%s)|%s|' %
          (x['ArchLink'], x['Name'], x['Link'], x['Description']))
