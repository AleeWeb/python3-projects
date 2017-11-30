
import json

people_string = '''
{
    "people": [
        {
            "name": "John Smith",
            "phone": "615-555-7164",
            "emails": ["johnsmith@bogusemail.com", "john.smithw@work.com"],
            "has_license": false
        },
        {
            "name": "Jane Doe",
            "phone": "560-555-5153",
            "emails": null,
            "has_license": true
        }
    ]
}
'''

print(people_string)
# print (len(people_string))  - Length method result is 385 characters long

# json.loads() function loads this string INTO a Python Object to work with data more easily
data = json.loads(people_string)  #Prints out everything horizontally bunched together
#print(data)
#print(type(data))   # Prints Out <class 'dict'>

#print(type(data['people']))  # People key prints Out  <class 'list'>


# --- Now I can loop through each person because this is a list --- 

for person in data['people']:
    print(person['name'])  #Prints out John Smith and Jane Doe


for person in data['people']:
    del person['phone']  # Delete all phone keys and values from Dictionary


# Dumps method - converts python object back into a string 
new_string = json.dumps(data, indent=2, #sort_keys=True)  # Dumps method places removed data back into the data dictionary
print(new_string)
