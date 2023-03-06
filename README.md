# maxval
About: Determines the maximum value or “net worth” of a group of bank accounts for a given tax year.

Status: This software is still under development and is in no way ready for use.

Explanation: The inspiration for this software came about because of IRS Form 8938 "Statement of Specified Foreign Financial Assets” which requires US citizens to report the total maximum value of all their foreign bank accounts during the tax year. This can be tricky because simply taking the sum of the highest balance for each account during the year doesn’t give the actual combined value or net worth of all the accounts.

For example: Let’s say you have bank account A with $400 and bank account B with $400. Now suppose you transfer $200 from account A and another $200 from account B into newly opened bank account C. The high balance for each account added together is $1200. Each of account had a high balance of $400 during the year. $400 x 3 = $1200. Yet the total maximum value, the net worth of the accounts is still only $800.

Eventually this software will read in multiple balance sheets which give account balances at various days over the course of a year.
