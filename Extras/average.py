#To find the average of numbers

count = 0
sum = 0
print("The numbers are : ")
for value in [20, 36, 1, 87, 27, 96,30, 49] :
	print(value)
	count = count + 1
	sum = sum + value
print("Average of the numbers : ",sum/count)