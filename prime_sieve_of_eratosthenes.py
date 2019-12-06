import time

default_prime_number = 0
number_value_start = int(input("Enter the start value : "))

if number_value_start % 2 == 0 or number_value_start < 2:
    print("Invalid data..Auto Set to Default value")
    number_value_start = 3
    default_prime_number = 2
    start_position = number_value_start
else:
    number_value_start = number_value_start + 1

number_value_end = int(input("Enter the end value : "))
if number_value_end < number_value_start:
    print("Invalid data..Auto Set to Default value")
    number_value = number_value_start + 1
start_time = time.time()

for numbers in range(number_value_start, number_value_end, 2):
    numbers_tmp = numbers
    print(numbers)

print("--- %s mins ---" % ((time.time() - start_time) / 60))
