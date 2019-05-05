"""
6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. 
Convert the extracted value to a floating point number and print it out.
"""

#Example program to use find() and strip()

text = "X-DSPAM-Confidence:    0.8475";
fpos = text.find(':')
#print(fpos)
str = text[fpos+1:]
#print(str)
value=float(str.lstrip())
print(value)