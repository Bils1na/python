# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

arr = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, 
       {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}]
arr_res = []
arr_res_2 = []

for i in arr:
    arr_res += list(i.values())

for i in range(len(arr_res)):
    arr_res[i] = arr_res[i].strip()

print(set(arr_res))