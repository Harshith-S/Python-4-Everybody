#Simple Python program using JSON

import json

data = '''{
	"name" : "Harshith",
	"id" : "485095"
}'''

info = json.loads(data)
print("Name : ",info['name'])
print("ID : ",info['id'])