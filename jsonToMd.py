#!/usr/bin/env python
import json

json_data = open('result.json').read()

data = json.loads(json_data)

print('|name|description|')
print('|---|---|')
for x in data:
    print('|[%s](%s) <small>[ArchLink](%s)</small>|%s|' %
          (x['Name'], x['Link'], x['ArchLink'], x['Description']))
