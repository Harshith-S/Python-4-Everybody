#To find the largest number in a given list

large = None				#None is a flag value. and you can use any word
print("The numbers are : ")
for value in [20, 36, 1, 87, 27, 96,30, 49] :
	print(value)
	if large is None:
		large = value
	elif value > large :
		large = value
print("Largest  number is : ",large)