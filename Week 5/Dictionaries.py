# Python Dictionary Examples
# This file demonstrates basic dictionary operations

# 1. Creating an empty dictionary
conversion_factor = {}
print("Empty dictionary:", conversion_factor)

# 2. Adding key-value pairs
conversion_factor["dollar"] = 60
conversion_factor["euro"] = 80

print("After adding items:", conversion_factor)

# # 3. Accessing a value using key
print("Value of euro:", conversion_factor["euro"])

# # 4. Getting all keys
print("Keys:", conversion_factor.keys())

# # 5. Getting all values
print("Values:", conversion_factor.values())

# # 6. Getting all key-value pairs
print("Items:", conversion_factor.items())

# # 7. Updating a value
conversion_factor["dollar"] = 65
print("After updating dollar value:", conversion_factor)

# # 8. Adding another currency
conversion_factor["yen"] = 50
print("After adding yen:", conversion_factor)

# # 9. Deleting a key-value pair
del conversion_factor["yen"]
print("After deleting yen:", conversion_factor)

# # 10. Currency conversion example
euro_amount = 30
rupees = euro_amount * conversion_factor["euro"]

print("30 Euros in Rupees =", rupees)