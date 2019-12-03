import threading
import time

start_time = time.time()


def hunt_prime(number_value_start_func, number_value_end_func):
    for numbers in range(number_value_start_func, number_value_end_func):
        is_prime = True
        for number in range(2, (int(numbers / 2) + 1)):
        #for number in range(2, numbers):
            mod_value = numbers % number
            if mod_value == 0:
                is_prime = False
                break
        if is_prime:
            global prime_number_count
            #print(numbers)
            prime_number_count += 1


number_value = 1000000
total_thread = 4
segment_number = int(number_value / 4)
# print(half_point_number)
prime_number_count = 0

# creating thread
number_value_start = 2
number_value_end = segment_number
print(f"t1 start {number_value_start}  end {number_value_end}")
t1 = threading.Thread(target=hunt_prime, args=(number_value_start, number_value_end,))
number_value_start = segment_number+1
number_value_end = segment_number*2
print(f"t2 start {number_value_start}  end {number_value_end}")
t2 = threading.Thread(target=hunt_prime, args=(number_value_start, number_value_end,))
number_value_start = segment_number*2+1
number_value_end = segment_number*3
print(f"t3 start {number_value_start}  end {number_value_end}")
t3 = threading.Thread(target=hunt_prime, args=(number_value_start, number_value_end,))
number_value_start = segment_number*3+1
number_value_end = number_value
print(f"t4 start {number_value_start}  end {number_value_end}")
t4 = threading.Thread(target=hunt_prime, args=(number_value_start, number_value_end,))
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()
print(f"Total prime numbers between 2-{number_value} is {prime_number_count}")
print("--- %s mins ---" % ((time.time() - start_time) / 60))
