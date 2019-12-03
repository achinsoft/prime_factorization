import numpy as np

number_value = 100000
prime_number_count = 0
for numbers in range(2, number_value):
    prime_check = True
    for number in range(2, numbers):
        mod_value = numbers % number
        if mod_value == 0:
            prime_check = False
            break
    if prime_check:
        prime_number_count += 1
print(f"Total prime numbers between 2-{number_value} is {prime_number_count}")