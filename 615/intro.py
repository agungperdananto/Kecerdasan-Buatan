trx = {
    "discount": 20,
    "disc_percentage": True,
    "tax": 2.5,
    "items":[
        {
        "product": "Gula pasir 1kg",
        "price": 10000,
        "qty": 2
        },
        {
        "product": "Aqua 500 ml",
        "price": 5000,
        "qty": 10
        },
        {
        "product": "Masako 50gr",
        "price": 1500,
        "qty": 4
        },
        {
        "product": "Garam 500gr",
        "price": 8000,
        "qty": 3
        }
    ]
}

# Subtotal
items = trx["items"]
subtotal = sum([item["price"] * item["qty"] for item in items])
diskon = subtotal * trx["discount"]/100 if trx["disc_percentage"] else trx["discount"]
pajak = (subtotal - diskon) * trx["tax"]/100
total = subtotal - diskon + pajak
# print("subtotal:", subtotal)
# print("total discount:", diskon)
# print("pajak:", pajak)
# print("grand total:", total)

# print(f"subtotal: Rp.{subtotal}" )
# print(f"total discount: Rp.{diskon}" )
# print(f"pajak: Rp.{pajak}" )
# print(f"grand total: Rp.{total}" )

# BILL
print(" BILL")
print("==============================")
print("item:")
item_no = 1
for item in items:
    product = item["product"]
    price = item["price"]
    qty = item["qty"]
    print(f"{item_no}. {product}: Rp.{price}")
    print(f"      qty: {qty}")
    print(f"                     subtotal: Rp.{price * qty}")
    print("--------------------------------")
    item_no += 1
print(f"                        subtotal: Rp.{subtotal}" )
print(f"                        total discount: Rp.{diskon}" )
print(f"                        pajak: Rp.{pajak}" )
print(f"                        grand total: Rp.{total}" )
