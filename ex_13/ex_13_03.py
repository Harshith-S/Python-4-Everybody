#Simple Python program using JSON2

import json

data = '''[
	{
		"name" : "Harshith",
		"id" : "485095"
	},
	{
		"name" : "Geetha",
		"id" : "485381"
	}
]'''

info = json.loads(data)
print("Count : ",len(info))

for item in info:
	print("Name : ",item['name'])
	print("ID : ",item['id'])