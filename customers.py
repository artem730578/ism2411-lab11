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


print ("-- Exercise 5 --")
tier_discounts = {
     "bronze": 0,
    "silver": 0.05,
    "gold": 0.1,
    "platinum": 0.15
}

purchase = 200
discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - discount_rate)
print(f"Tier: {customer['tier']}")
print(f"Discount Rate: {discount_rate * 100:.0f}%")
print(f"Final Price: ${final_price:.2f}")

print("-- Exercise 6 --")
customers = [
    {"name": "Alice", "tier": "platinum"},
    {"name": "Ben", "tier": "silver"},
    {"name": "Carla", "tier": "bronze"}
]

for c in customers:
    rate = tier_discounts.get(c["tier"], 0)   # look up the discount for this tier
    discount_amount = 300 * rate               # discount on a $300 purchase
    print(f"{c['name']} | Tier: {c['tier']} | Discount on $300: ${discount_amount:.2f}")


print("-- Exercise 7 --")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}

for product_name, product_details in catalog.items():
    if product_details["stock"] < 20:
        print(f"LOW STOCK: {product_name} ({product_details['stock']} left)")


print("-- Exercise 8 --")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

summary = {}
for t in transactions:
    region = t["region"]
    summary[region] = summary.get(region, 0) + t["amount"]   # add to the running total

for region in sorted(summary):
    print(f"{region}: {summary[region]}")