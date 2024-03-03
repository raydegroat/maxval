#! /usr/bin/env python3
# Maxval accounts value evaluator - Raymond de Groat, 2023 https://github.com/raydegroat

# import sys
import datetime
from pathlib import Path
import csv

# Create a new output file on each run
f = open('daily_totals.csv', 'w')
f.close

# Directory where bank csv files are stored
dir_name = '../account_history'

TAX_YEAR = 2022

# Using datetime to make a list of days in the TAX_YEAR
JAN1_TAX_YEAR = datetime.date(TAX_YEAR, 1, 1 )
DEC31_TAX_YEAR = datetime.date(TAX_YEAR, 12, 31)
aday = datetime.timedelta(days=1)
thedate = JAN1_TAX_YEAR
TAX_YEAR = []

while (thedate <= DEC31_TAX_YEAR):
    TAX_YEAR.append(str(thedate))
    thedate += aday

# Creating a list of dictionaries to store account data for each day of the year
daily_reports = []
for date in TAX_YEAR:
    daily_report = dict(date = date, accounts = [])
    daily_reports.append(daily_report)

# Getting a listing of all .csv files in directory dir_name and the generated list to a more permanent list[]
dir_list = Path(dir_name).glob('*.csv')
file_list = []
for file in dir_list:
    file_list.append(file)

# Using the file name to name the accounts and assiging an initial balance of None
for acc_name in file_list:
    for report in daily_reports:
        report['accounts'] += [{'account' : acc_name.stem, 'balance' : None}]


# Reading files, comparing dates and setting balances.
idx = 0
for acc_name in file_list:
    bal = 0
    print(acc_name.stem)
    for report in daily_reports:
        with open(acc_name, 'r') as f:
            csvFile = csv.reader(f)
            for row in reversed(list(csvFile)):
                if report['date'] == row[0].replace(" ", ""):
                    bal = row[2].replace(" ", "")
                    report['accounts'][idx]['balance'] = bal
                else:
                    report['accounts'][idx]['balance'] = bal
    idx += 1

# Get the total number of accounts for user reality check
num_accounts = len(report['accounts'])

# Read daily_totals, calcluate totol daily totals and output to the screen
daily_totals = []
for report in daily_reports:
    daily_total = 0
    print(report['date'])
    for idx in range(len(report['accounts'])):
        print(report['accounts'][idx]['account'], report['accounts'][idx]['balance'])
        daily_total += int(report['accounts'][idx]['balance'])
    print("-------------------")
    print("Daily total: ", str(daily_total))
    daily_totals.append(daily_total)
    print()

# Display the number of accounts and the highest daily value of all accounts
maxVal = max(daily_totals)
print("There are", num_accounts, "accounts.")
print("The maximum daily amount of all account total is: ", maxVal)

# Write the account names with dates and balances to a .csv file
with open('daily_totals.csv', 'a') as f:
    f.write('Account name: ')
    f.write(',')
    for idx in range(len(report['accounts'])):
        f.write(report['accounts'][idx]['account'])
        f.write(',')
    f.write('Daily total')
    f.write('\n')

    for report in daily_reports:
        daily_total = 0
        f.write(report['date'])
        f.write(',')
        for idx in range(len(report['accounts'])):
          daily_total += int(report['accounts'][idx]['balance'])
          f.write(str(report['accounts'][idx]['balance']))
          f.write(',')
        f.write(str(daily_total))
        f.write('\n')

# print("The following accounts had no starting balance for January 1, 2024 and were skipped.")
# for i in no_start_bal:
#     print(i)
