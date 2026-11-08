# customers.py
# Author Artem
# Module 11 Lab: Customer Dictionary & Lookup


print("-- Exercise 1 --")
customer = {
    "name": "Alice", #Key : Value,
    "Name": "Not-Alice",
    'email': "alice@example.com",
    "tier": "gold",
    "ytd_spend": 12400,
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)

print("-- Exercise 2 --")
customer['phone'] = '555-5555' #Adding a new key value pait to the dictionary
print(customer)
customer['tier'] = 'platinum' #Updating the value of an existing key
print(customer)
del customer['email'] #Deleting a key value pair from the dictionary
del customer['Name'] #Deleting a key value pair from the dictionary
print(customer)



print("-- Exercise 3 --")
print(customer.get("email", "no email on file"))
try:
    print(customer["email"])
except KeyError as e:
    print("KeyError:", e)


print("-- Exercise 4 --")
for key, value in customer.items():
    print(f"{key}: {value}")

for key in customer:
    print(key)
# Without .items(), the loop only gives the keys, not the values.
# To get the value that way I have to write customer[key] inside the loop.