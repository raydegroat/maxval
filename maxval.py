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

    
      


# daily_report.


# dir_list = Path(dir_name).glob('*.csv')
# for i in dir_list:
#     account_names.append(i.stem)

# for day in taxYear2022:
#     # daily_report[day] += [{'accounts' : acc_name, 'balance' : None}]
#     print(daily_report[day])

# for dates in taxYear2022:
#     for acc_name in account_names:
#         daily_report[dates] = [{acc_name : '20000000'}]

# for i in daily_report.items():
#     print(i)
# print(daily_report)

# for i in daily_report.items():
#     print(i)

# print(daily_report['accounts'])

# dir_list = Path(dir_name).glob('*.csv')
# for file in dir_list:
#     acc_name = file.stem
#     for i in daily_report.update({accounts[{acc_name : 0}]}):
#         print(i)
        # i['accounts'] += [{acc_name : 0}]

# for i in daily_report.items():
#     print(i)


#     for date in taxYear2022:
#         daily_report[date] += [{'accounts' : acc_name}]

# for i in daily_report.values:
#     print(i)



# daily_report["2022-06-26"] = [{"Raybase" : "250000"}]
# daily_report["2022-06-26"] += [{"MyBase" : "1000000"}]

# daily_reports = []

# bal = 0
# for date in taxYear2022:
#     daily_report = dict(date = date, accounts = [])
    
    
#         with open(file, 'r') as f:
#             csvFile = csv.reader(f)
#             for row in reversed(list(csvFile)):
#                 if row[0] == date:
#                     bal = row[2]
#             daily_report['accounts'] += [{'account' : acc_name, 'balance' : bal}]
#         daily_reports.append(daily_report)
# count = 0

# for i in daily_reports:
#     print(i)
#     print(count)
#     count += 1                
        
