# ISM2411 Lab 11 - Customer Dictionary & Lookup
# Name: Carolyn F.

# Reflection 1:
# I would use .get() when a key might be missing and I want to provide
# a default value instead of causing an error. I would use bracket notation
# when I know the key exists and need to access its value directly.

# Reflection 2:
# Exercise 8 reminds me of using SUMIF in Excel because it adds values
# based on a category. Python is more useful for large datasets because
# it can automatically process many records and create summaries with a loop.


# EXERCISE 1 - One customer

customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1250
}

print("EXERCISE 1")
print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)


# EXERCISE 2 - Update and add

print("\nEXERCISE 2")

customer["phone"] = "555-123-4567"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)


# EXERCISE 3 - Safe lookup

print("\nEXERCISE 3")

email = customer.get("email", "no email on file")
print(email)

try:
    print(customer["email"])
except KeyError:
    print("KeyError: email does not exist")


# EXERCISE 4 - Iterate

print("\nEXERCISE 4")

for key, value in customer.items():
    print(f"{key}: {value}")

# Without .items(), the loop only gives the keys.
for key in customer:
    print(key)


# EXERCISE 5 - Lookup table

print("\nEXERCISE 5")

tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}

tier = customer["tier"]
discount = tier_discounts.get(tier, 0)
purchase = 200
final_price = purchase - (purchase * discount)

print("Tier:", tier)
print("Discount rate:", discount * 100, "%")
print("Final price: $", round(final_price, 2))


# EXERCISE 6 - List of dicts

print("\nEXERCISE 6")

dict1 = {
    "name": "Alice",
    "tier": "platinum"
}

dict2 = {
    "name": "Bob",
    "tier": "gold"
}

dict3 = {
    "name": "Charlie",
    "tier": "silver"
}

customers = [dict1, dict2, dict3]

for customer in customers:
    tier = customer["tier"]
    discount_rate = tier_discounts.get(tier, 0)
    discount_amount = 300 * discount_rate

    print(
        f"{customer['name']}: {tier} - "
        f"Discount: ${discount_amount:.2f}"
    )


# EXERCISE 7 - Nested catalog

print("\nEXERCISE 7")

catalog = {
    "Widget A": {
        "price": 9.99,
        "stock": 150
    },
    "Gadget C": {
        "price": 49.99,
        "stock": 8
    }
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product} - Stock: {details['stock']}")


# EXERCISE 8 - Sales by region

print("\nEXERCISE 8")

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

sales_summary = {}

for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]

    sales_summary[region] = sales_summary.get(region, 0) + amount

for region in sorted(sales_summary):
    print(f"{region}: ${sales_summary[region]}")