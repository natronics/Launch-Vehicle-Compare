#!/usr/bin/env python
from os import walk
import json

f = []
for (dirpath, dirnames, filenames) in walk('./metadata'):
    f.extend(filenames)
    break

with open('index.markdown', 'w') as fout:
    fout.write("""---
layout: base
title: Launch Vehicle Compare
---

# Launch Vehicles
""")

    for fname in f:
        with open('./metadata/'+fname, 'r') as fin:
            metadata = json.loads(fin.read())
            fout.write('## '+metadata['name']+'\n\n')
            fout.write('![image](vehicles/'+metadata['svg']+')\n\n')
