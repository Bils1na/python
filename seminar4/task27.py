import string
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells


text = """She sells sea shells on the sea shore The shells
that she sells are sea shells I'm sure.So if she sells sea
shells on the sea shore I'm sure that the shells are sea
shore shells"""

text = text.split()
count = 0

for i in range(len(text)):
    if not text[i].isalpha():
        text[i] = " ".join(text[i].split("."))
        
    # print(i, end = " ")
print(set(text))
