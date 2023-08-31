sp = [55, 44, 'hello', True, 99.88, 100]

# for i in range(len(sp)):
#     print(sp[i])

# for item in sp:
#     print(item)

# for i, v in enumerate(sp):
#     print(i, v)

# print("hello" in sp)

# sp.append("last")
# sp.insert(0, "zero")
# # sp.extend([1, 2, 3])
# sp += [0] * 10
# print(sp)

# del sp[0]
# sp.remove(True)
# a = sp.pop()
# print(a)
# print(sp)
# print(len(sp))

# list tuple set dict

# t = (5, 7, "privet",)
# print(type(t))
# print(len(t))
# print(t[0])

# s = {8, 8, 8}
# s.add(777)
# s.discard(7777)
# print(s)

# d = {123: 5424534, "ira": [42363, 4355]}
# d["vanya"] = 15425
# d[input("Enter name >> ")] = input("Enter phone number >> ")
# d["ira"].append(356457)
# print(d)

# del d[123]
# print(d)

# print(d.keys(), d.values())

# for k in d:
#     print(k)

# for key, value in d.items():
#     print(f"{key} - {value}")

# сколько раз встречается конкретная цифра в этом списке?
# sp = [55.1245, 44, "Spyyyyy55", [95.45, 0.5], {53: 125}]
# ответ будет 11 для цифры 5

sp = [55.1245, 44, "5pyyyyy55", [95.45, 0.5], {53: 125}]
x = str(sp)
print(x)
count = 0

for i in x:
    if i == "5":
        count += 1

print(f"Цифра 5 встречается в списке {count} раз")