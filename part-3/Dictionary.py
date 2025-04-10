thisDict ={"id" : 1, "name" : "Jen", "Salary" : 500000.00}

print(thisDict)
print(type(thisDict))

print(thisDict["name"])

thisDict ["Salary" ] = 780000
thisDict ["id"]= 2


print(thisDict)



# adding other collection 

thisDict["address"] = {"street" : "123 Main St", "city" : "New York"}

print(thisDict)

# deleting a key

del thisDict["address"]

print(thisDict)


# another collection 

thisDict ["Numbers"] = {"077895940, 77895940, 77895940, 77895940"}

print(thisDict)

thisDict [ "Address"] = {"Colombo", "Jaffna", "Kandy"}
print(thisDict)

thisDict["Address"] = {"street": "Colombo", "city": "Jaffna", "region": "Kandy"}
print(thisDict["Address"]["street"])  
