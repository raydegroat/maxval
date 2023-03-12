# maxval
About: Determines the maximum value of a group of bank accounts for a given tax year.

Status: This software is still under development and is in no way ready for use.

Explanation: Adds the balance of all accounts for tax year 2022 to get the total balance for each day. This is the "total daily balance". There are 365 total daily balances, one total balance for each day of the year. The highest of these daily balances is then reported. This is the maximum value of all accounts for that year.

Background: The inspiration for this software came about because of IRS Form 8938 "Statement of Specified Foreign Financial Assets” which requires US citizens to report the total maximum value of all their foreign bank accounts during the tax year. Simply taking the sum of the highest balance for each account during the year doesn’t give the actual combined value or net worth of all the accounts. Suppose you often transfer money between your savings and your checking. Or suppose you closed an account with $1000 and opened a new account in the same year with the same $1000. Simply adding up the high balance from each account during the year will count this same $1000 twice.

Usage: Currently there is no front-end for this program. The program requires input from .csv files (comma separated value) and should be stored in a directory named ‘account_history’. 

The CVS file format is "date, amount, balance".

Date is in the format "yyyy-mm-dd".
The ‘amount’ is the transaction amount plus or minus. This column is currently unused but must be present.
The 'balance’ is the account balance after the transaction. This would be 3 columns in a spreadsheet.

Entries should be listed in reverse chronological order, one per row.

2022-02-25, 45000, 102792

2022-02-25, -150, 57792

2022-01-27 -35, 57942

2022-01-01,, 57977

The can be no thousandths separator or commas in the fields and there must be a starting balance for January 1, 2022. If no starting balance is provided for January 1, the balance will be consider zero until the first entry. The output will be a file named daily_totals.csv which can be opened as a spreadsheet. Column A will contain the dates of the year in reverse starting with December 31. The remaining columns will contain the account names with their corresponding daily balances.
