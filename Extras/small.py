#To find the smallest number in a given list

small = None				#None is a flag value. and you can use any word
print("The numbers are : ")
for value in [20, 36, 1, 87, 27, 96,30, 49] :
	print(value)
	if small is None:
		small = value
	elif value < small :
		small = value
print("smallest  number is : ",small)