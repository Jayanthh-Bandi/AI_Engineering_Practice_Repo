# import json

# order_json='''
# {
#     "order_id": 12345,
#     "customer": "John Doe",
#     "status": "Processing"
# }
# '''
# order_data=json.loads(order_json)

# print(order_data["customer"])
# print(order_data["status"])

import json

order = {
    "order_id": 1052,
    "customer": "priya",
    "status": "Shipped",
    "Payment_status":"Paid"
}

with open("order.json","w") as file:
    json.dump(order,file,indent=4)