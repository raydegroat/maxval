#! /usr/bin/env python3
# Maxval accounts value evaluator - Raymond de Groat, 2023 https://github.com/raydegroat

import pandas as pd
import datetime
from pathlib import Path
import os

# Directory where bank csv files are stored
dir_name = 'account_history'
days = []

# Using datetime to make a list of days in the year
Jan1_2022 = datetime.date(2022, 1, 1 )
Dec31_2022 = datetime.date(2022, 12, 31)
aday = datetime.timedelta(days=1)
thedate = Jan1_2022

while (thedate <= Dec31_2022):
    days.append(thedate)
    thedate += aday


# Use Path to get files ending in .csv
dir_list = Path(dir_name).glob('*.csv')
for file in dir_list:

    print(file.name)
    f = open(file, 'r')
    lines = f.readlines()
    for line in reversed(lines):
        print(line.rstrip())
