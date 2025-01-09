##
# Program that creates a dictionary called person containing data from the two other 
# dictionaries (five key-value pairs). Print the contents of the ‘person’ dictionary
##

basic_data = {
   "name":"Barbara",
   "age":21
}

advanced_data = {
   "status":"student",
   "married":False,
   "interest":["reading","swimming"]
}
person = basic_data.copy()
person.update(advanced_data)
# possible -> person = {**basic_data, **advanced_data}

print(person)
