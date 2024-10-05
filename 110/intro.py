# List = [1, 2, 3]

#  Dictionary = {key: value}

data_list = [i + 2 for i in range(12)]
print(data_list)

# 10
print(data_list[8])

data_dict = {
    "nama": "Ari",
    "nilai": 55,
    "lulus": False
}

kelulusan = "LULUS" if data_dict["lulus"] else "TIDAK LULUS"
nama = data_dict["nama"]
print(f"Mahasiswa dengan nama {nama} dinyatakan {kelulusan}")