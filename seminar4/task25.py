# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

def count_similar(val_str):
    val_str = val_str.split()
    count = 0

    for i in val_str:
        for j in range(val_str.index(i) + 1, len(val_str)):
            if val_str[j] == i:
                count += 1
                val_str[j] += f"_{count}"
        count = 0
    
    print(*val_str)


text = "a a a b a c a a d c d d c d"

count_similar(text)
