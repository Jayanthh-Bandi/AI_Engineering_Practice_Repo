




def calculate_delivery_fee(order_amount):

    if order_amount >= 500:
        return 0
    else:
        return 40


fee = calculate_delivery_fee(250)

print(fee)

customers={
    "Id":101,
    "name":"John Doe",
    "email":"John.Doe@example.com",
    "location":"Bangalore",
    "membership":"Premium"
}

print(customers["email"])
print(customers["membership"])

customers["membership"] = "Gold"
customers["city"] = "Hyderabad"

customers = [
    {"id": 101, "name": "John", "city": "Hyderabad"},
    {"id": 102, "name": "Priya", "city": "Mumbai"},
    {"id": 103, "name": "Rahul", "city": "Bangalore"},
    {"id": 104, "name": "Ananya", "city": "Chennai"}
]

for customer in customers:
    print(customer["name"], "-", customer["city"])

print(customers[1]["name"])