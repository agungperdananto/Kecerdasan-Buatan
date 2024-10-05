# list

#create 0-100 into data list
data_list = [i for i in range(100)]

# Dictionary

# cashback / discount
coupons = [{
    "type": "discount",
    "value": 20000,
    "percentage": False
},
{
    "type": "discount",
    "value": 20,
    "percentage": True
}
]

data_dict = {
"items": [
    {
        "price": 50000,
        "qty": 3
    },
    {
        "price": 15000,
        "qty": 2
    },
    {
        "price": 40000,
        "qty": 1
    },
]
}

subtotal = 0

# hitung subtotal masing2
# for item in data_dict["items"]:
#     subtotal += item["price"] * item["qty"]

subtotal = sum([ item["price"] * item["qty"] for item in data_dict["items"]])

# total = subtotal - (subtotal * coupon["value"] /100 ) if coupon["percentage"] else subtotal - coupon["value"]
total = subtotal
for coupon in coupons:
    print(coupon["value"])
    if coupon["type"] == "discount":
        total = total - (total * coupon["value"] /100 ) if coupon["percentage"] else total - coupon["value"]

# 0,1,2,3,4,5,6,7...99
print("List:", data_list[5:8])

print("items:", data_dict["items"])
print("subtotal:", subtotal)
print("total setelah discount:", total)


# Perlu diinstall adalah:
# jupyter
# matplotlib
# dibuat virtualenv dan diactifkan
# pip install jupyter