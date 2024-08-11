data = {"n": 1500, "m": 2, "CLUSTERS": 3, "ITER": 10000, "METHOD": "FCM", "MEASURE": "EUCLIDEAN", "YEARS": 51}
print(data)
data["MEASURE"] = "MANHATAN"
print(data)
print(data["METHOD"])
data["LOSS FUNCTION"] = "NORM_2"
print(data)
del data["YEARS"]
print(data)
s = input("Nhập xâu S: ")
print("Trùng" if s in data.values() else "Không trùng")
print(set(data.values()))
print(list(data.values()))
