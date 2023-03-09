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

# Getting a listing of all .csv files. The name of each file fill be used as the account name
dir_list = Path(dir_name).glob('*.csv')

# Adding account names to the dictionaies with an initial balance of None
for acc_name in dir_list:
    print(acc_name.name)
    for report in daily_reports:
        report['accounts'] += [{'account' : acc_name.name, 'balance' : None}]

# Testing...
for report in daily_reports:
    if report['date'] == '2022-01-20':
        print(report)
        print(report.items())
