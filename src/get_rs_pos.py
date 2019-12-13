#!/usr/bin/env python
import json
from m2zfast import getConf, getSettings

opts, args = getSettings()


print(json.dumps([
    {'chrom': chrom, 'start': start, 'end': end}
    for snp, chrom, start, end in opts.snplist
]))