# Key cannot be duplicated

customer = {
    "name": "Jinho Jo",
    "age" : 30,
    "is_verified": True
}
print(customer)
print(customer["name"])
print(customer["age"])
print(customer["is_verified"])
# print(customer["haha"]) # KeyError: 'haha'
print(customer.get("haha"))
print(customer.get("birthday", "1994-6-20"))
customer["name"] = "Hola"
print(customer)
customer["birthdate"] = "1994-6-20"
print(customer.get("birthdate"))
print(customer)
print(customer.pop("name"))
print(customer)
print(customer.items())
print(customer.keys())
print(customer.values())
# print(customer.clear())
print(customer)
print(customer.popitem())

