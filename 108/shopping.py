
transaksi = {
    "discount": 20,
    "percentage": True,
    "items":[
        {
        "price": 10000,
        "qty": 2
        },
        {
        "price": 5000,
        "qty": 12
        },
        {
        "price": 120000,
        "qty": 3
        }
    ]
}

# tambah item
transaksi["items"].append({"price": 20000, "qty": 5})
print(transaksi["items"])

# Hitung subtotal (sebelum diskon), total(setelah diskon)
# subtotal = sum([item["price"] * item["qty"] for item in transaksi["items"]])
# print("subtotal:", subtotal)
# print("total:", subtotal - (subtotal * transaksi["discount"]/100) if transaksi["percentage"] else subtotal - transaksi["discount"])
subtotal = sum([item["price"] * item["qty"] for item in transaksi["items"]])
diskon = (subtotal * transaksi["discount"]/100) if transaksi["percentage"] else transaksi["discount"]
results = {
    "subtotal": subtotal,
    "diskon": diskon,
    "total": subtotal - diskon
}

results["pajak"] = 2.5/100 * results["total"]

for k, v in results.items():
    print(f"{k}: Rp.{v}")
