#! /usr/bin/env python3
# Maxval accounts value evaluator - Raymond de Groat, 2023 https://github.com/raydegroat

import pandas as pd
from pathlib import Path
import os

dir_name = 'account_history'

year2022 = pd.date_range(start='1/1/2022', end='12/31/2022')

# Use Path to get files ending in .csv
dir_list = Path(dir_name).glob('*.csv')
for file in dir_list:
    print(file.name)
    f = open(file, 'r')
    lines = f.readlines()
    for line in reversed(lines):
        print(line.rstrip())
