#! /usr/bin/env python3
# Maxval accounts value evaluator - Raymond de Groat, 2023 https://github.com/raydegroat

import pandas as pd
import datetime
from pathlib import Path
import csv
import os

# Directory where bank csv files are stored
dir_name = 'account_history'

# Using datetime to make a list of days in the year
Jan1_2022 = datetime.date(2022, 1, 1 )
Dec31_2022 = datetime.date(2022, 12, 31)
aday = datetime.timedelta(days=1)
taxYear2022 = []
thedate = Jan1_2022

while (thedate <= Dec31_2022):
    taxYear2022.append(str(thedate))
    thedate += aday

daily_reports = []

bal = 0
for date in taxYear2022:
    daily_report = dict(date = date, accounts = [])
    dir_list = Path(dir_name).glob('*.csv')
    for file in dir_list:
        acc_name = file.stem
        with open(file, 'r') as f:
            csvFile = csv.reader(f)
            for row in reversed(list(csvFile)):
                if row[0] == date:
                    bal = row[2]
            daily_report['accounts'] += [{'account' : acc_name, 'balance' : bal}]
        daily_reports.append(daily_report)
count = 0

for i in daily_reports:
    print(i)
    print(count)
    count += 1                
        
