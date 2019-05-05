"""
Finding Numbers in a Haystack

In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.
Data Files
We provide two files for this assignment. 
One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
Actual data: http://py4e-data.dr-chuck.net/regex_sum_208835.txt (There are 94 values and the sum ends with 448)
"""

import re

name = input("Enter the file : ")
handle = open(name)

result=list()							#Empty list(Because the result of findall() is a list, it'll be easy to add)
for line in handle:
	number=re.findall('[0-9]+',line)	#Extract the numbers from file and store it in numbers
	result=result+number				#append the numbers found using the regex in this list

sum=0
for i in result:
	sum=sum+int(i)						#find the sum

print(sum)