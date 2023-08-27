# Задача 1 HARD по желанию Напишите программу,
# которая принимает на вход целое или дробное 
# число и выдаёт количество цифр в числе.
# 456 -> 3
# 0 -> 1
# 89,126 -> 5
# 0,001-> 4

def count_digits(number):
    num_digits = 0

    if number == 0:
        num_digits = 1 
    else:
        
        if number < 0:
            number = -number

        while number > 0:
            number //= 10
            num_digits += 1

    return num_digits

def fractional_part_len(number_to_count):
    count = 0
    
    while number_to_count % 1 != 0:
        number_to_count *= 10
        count += 1
    
    return count
    

number = float(input("Enter number >> "))
digit_count = count_digits(number)

print(f"{digit_count + fractional_part_len(number)}")