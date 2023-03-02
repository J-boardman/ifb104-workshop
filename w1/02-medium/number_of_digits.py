# Number of Digits
#
# THE PROBLEM
#
# You have to number all the pages in a book which has a total
# of 366 pages.  Write a Python script to calculate how
# many individual digits you have to write down.  (NB: You are
# not expected to write "leading zeros" before the page numbers.)
#
# Ask yourself how many page numbers will have one digit, how
# many have two digits, and so on.  Hint: In an inclusive range
# of numbers from M to N there are (N - M) + 1 distinct values.
# For instance, there are (99 - 10) + 1 = 90 numbers in the range
# from 10 to 99, inclusive.

#### Complete your solution by replacing the zeros below

# First work out how many pages there are with one, two and three digits
total_digits = 0
total_pages = 366

# Add page since range(total_pages) will stop at 365
for page in range(total_pages + 1):
    # Skip over page 0
    if page == 0:
        continue
    
    # convert page number to a string, break into array to iterate over digits
    split_pages = list(str(page)) 
    for i in split_pages:
        total_digits += 1

one_digit_pages = 9
# 99 - 10 + 1
two_digit_pages = 90
# 366 - 100 + 1
three_digit_pages = 267

total_digits_exp = one_digit_pages + (two_digit_pages * 2) + (three_digit_pages * 3)

print ('You will have to write', total_digits, 'digits')
print ('You will have to write', total_digits_exp, 'digits')
