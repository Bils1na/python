# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6 


def define_fib_number(number):
    digit_one = 0
    digit_two = 1
    digit_three = digit_one + digit_two
    count = 3
    if number == digit_one:
        return 1
    if number == digit_two:
        return 2

    while digit_three < number:
        digit_one = digit_two
        digit_two = digit_three
        digit_three = digit_one + digit_two
        count += 1

    if digit_three == number:
        return count    
    else:
        return -1


try:
    number = int(input("Enter your number >> "))

    print(f"{number} = {define_fib_number(number)}")
except: 
    print("Error!")
