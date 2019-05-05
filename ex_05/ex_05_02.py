"""
5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
Once 'done' is entered, print out the largest and smallest of the numbers. 
If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
Enter 7, 2, bob, 10, and 4 and match the output below.
"""

large = None
small = None
while True:
	sval = input("Enter a number: ")			#sval=string value.
	if sval == "done":
		break
	try:
		fval = float(sval)							#fval = float value
	except:
		print("Invalid input")
		continue
	if small is None:
		small = fval
	if large is None:
		large = fval
	if fval > large:
		large = fval
	if fval < small:
		small = fval

print("Maximum is", int(large))
print("Minimum is", int(small))