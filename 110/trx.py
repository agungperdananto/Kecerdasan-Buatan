trx = {
    "items": [
        {
            "product": "Aqua 500ml",
            "price": 5500,
            "qty": 3
        },
        {
            "product": "Indomie goreng",
            "price": 3200,
            "qty": 12
        },
        {
            "product": "Gula Pasir 1kg",
            "price": 17000,
            "qty": 2
        },
    ],
    "discount": 15,
    "tax": 11
}

print(trx["discount"])

# subtotal, nominal diskon, nominal pajak, & grand_total

print("================================================")
print("                     BILL")
print("================================================")
print("Items:")
subtotal = 0
for item in trx["items"]:
    product = item["product"]
    price = item["price"]
    qty = item["qty"]
    print(f"                {product}  : Rp. {price}")
    print(f"                             x {qty} pcs      Rp {price * qty}")
    print("----------------------------------------------------")
    subtotal += price * qty

print(f"                                    Subtotal Rp.{subtotal}")
discount = subtotal * trx["discount"] /100
print(f"                                    Diskon Rp.{discount} (-)")
tax = (subtotal - discount) * trx["tax"] /100
print(f"                                    Pajak Rp.{tax} ")
grand_total = subtotal - discount + tax
print("-----------------------------------------------------------------")
print(f"                                    GrandTotal Rp.{grand_total} ")