# -*- coding: utf-8 -*-

import csv
import json

data = []
with open('../data/KEN_ALL_ROME.CSV') as f:
    reader = csv.reader(f)
    for row in reader:
        data.append({
            "postalCode": row[0],
            "prefecture": row[1].replace('　', ' ').replace('以下に掲載がない場合', ''),
            "city": row[2].replace('　', ' ').replace('以下に掲載がない場合', ''),
            "street": row[3].replace('　', ' ').replace('以下に掲載がない場合', '')
        })

with open('../data/japanese-postal-code.json', mode='w') as f:
    f.write(json.dumps(data, indent=2, ensure_ascii=False))
