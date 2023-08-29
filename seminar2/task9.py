# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120 

def show_factorial(number):
    i = 1
    result = 1

    while i <= number:
        result *= i
        i += 1

    return result


number = int(input("Enter your number >> "))

print(f"{number}! = {show_factorial(number)}")
