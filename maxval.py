#! /usr/bin/env python3
# Maxval accounts value evaluator - Raymond de Groat, 2023 https://github.com/raydegroat

import pandas as pd
import datetime
from pathlib import Path
import csv
import os

# Directory where bank csv files are stored
dir_name = 'account_history'
days = []

# Using datetime to make a list of days in the year
Jan1_2022 = datetime.date(2022, 1, 1 )
Dec31_2022 = datetime.date(2022, 12, 31)
aday = datetime.timedelta(days=1)

# Use Path to get files ending in .csv
dir_list = Path(dir_name).glob('*.csv')

for account in dir_list:
    thedate = Jan1_2022
    print(account.stem)

    
    while (thedate <= Dec31_2022):
        with open(account, 'r') as f:
            csvFile = csv.reader(f)

            # print(thedate)
            for row in reversed(list(csvFile)):
                # print(str(thedate), "<----- Current date")
                # print(row[0], "<----- Date of new balance")
                if row[0] == str(thedate):
                    print(str(thedate), "<----- Current date")
                    print(row[0], "<----- Date of new balance")
                    print("Match found!!!!")
                    print()

        thedate += aday


        
