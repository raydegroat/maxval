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
thedate = Jan1_2022
taxYear2022 = []

while (thedate <= Dec31_2022):
    taxYear2022.append(str(thedate))
    thedate += aday

# Creating a list of dictionaries to store account data for each day of the year
daily_reports = []
for date in taxYear2022:
    daily_report = dict(date = date, accounts = [])
    daily_reports.append(daily_report)

# Getting a listing of all .csv files. Stoing the generated list to a more permanent list[]
dir_list = Path(dir_name).glob('*.csv')
file_list = []
for file in dir_list:
    file_list.append(file)

# Using the file name to name the accounts and assiging an initial balance of None
for acc_name in file_list:
    for report in daily_reports:
        report['accounts'] += [{'account' : acc_name.stem, 'balance' : None}]

# Getting list of .csv files AGAIN because... reasons? Path returns type generater?

count = 0
# Reading files. Comparing dates and getting balances.
for acc_name in file_list:
    bal = 0
    print(acc_name.stem)
    for report in daily_reports:
        with open(acc_name, 'r') as f:
            csvFile = csv.reader(f)
            for row in reversed(list(csvFile)):
                if report['date'] == row[0]:
                    print(row)
                    bal = row[2]
                    # print(bal)
                    print(report)
                    # print(report['accounts'][0]['balance'])
                    report['accounts'][count]['balance'] = bal
                    print(report)
                    # print(report['accounts'][0]['balance'])
                    # print(len(report['accounts']))
                    # print(report.values())
                    # print(row[2]
                else:
                    report['accounts'][count]['balance'] = bal
    count += 1
                    
          
        
