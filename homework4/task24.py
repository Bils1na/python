from random import randint
# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них 
# выросло различное число ягод — на i-ом кусте выросло a[i] ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, 
# которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном списке урожайности грядки.

def fill_list(length):
    result = [randint(1, 9) for i in range(length)]
    
    return result
    
def define_max_berries(number_berries):
    result = 0
    
    for i in range(1, len(number_berries) - 1):
        if number_berries[i-1] + number_berries[i] + number_berries[i + 1] > result:
            result = number_berries[i-1] + number_berries[i] + number_berries[i + 1]
            
    return result
    
    

bushes = int(input("Enter length >> "))
berries = fill_list(bushes)
max_berries = [berries[i-1]+berries[i]+berries[i+1] for i in range(1, len(berries) - 1)]

print(f"Number of the berries on the bushes {berries}")
print(f"Maximum amout of the berries {max_berries}")
print(f"Maximum = {define_max_berries(berries)}")