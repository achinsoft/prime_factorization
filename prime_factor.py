import threading
import time

start_time = time.time()

'''

# starting thread 1
t1.start()
# starting thread 2
t2.start()

# wait until thread 1 is completely executed
t1.join()
# wait until thread 2 is completely executed
t2.join()

# creating thread
t1 = threading.Thread(target=print_square, args=(10,))
t2 = threading.Thread(target=print_cube, args=(10,))
'''


def hunt_prime(number_value_start, number_value_end):
    for numbers in range(number_value_start, number_value_end):
        is_prime = True
        for number in range(2, (int(numbers / 2) + 1)):
            mod_value = numbers % number
            if mod_value == 0:
                is_prime = False
                break
        if is_prime:
            global prime_number_count
           # print(numbers)
            prime_number_count += 1


number_value = 100000
half_point_number = int(number_value / 2)
#print(half_point_number)
prime_number_count = 0

# creating thread
number_value_start = 2
number_value_end = half_point_number
t1 = threading.Thread(target=hunt_prime, args=(number_value_start, number_value_end,))
number_value_start = half_point_number
number_value_end = number_value
t2 = threading.Thread(target=hunt_prime, args=(number_value_start, number_value_end,))
t1.start()
t2.start()
t1.join()
t2.join()
print(f"Total prime numbers between 2-{number_value} is {prime_number_count}")
print("--- %s mins ---" % ((time.time() - start_time) / 60))
