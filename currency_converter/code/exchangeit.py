"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and amount.
It prints out the result of converting the first currency to the second.

Author: I-Chia Liao
Date:   2023-08-03
"""

import currency

# Ask user for input
src = input("3-letter code for original currency: ")
dst = input("3-letter code for the new currency: ")
amt = float(input("Amount of the original currency: "))


# Execute exchange function
dst_amt = currency.exchange(src,dst,amt)
round_dst_amt = round(dst_amt, 3)


# Print the result (E.g. You can exchange 2.5 USD for 2.216 EUR.)
print('You can exchange '+ str(amt) + ' ' + src + ' for ' + str(round_dst_amt) + 
' ' + dst + '.')
