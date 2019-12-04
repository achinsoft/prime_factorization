import threading
import time

start_time = time.time()


def hunt_prime(number_value_start_func, number_value_end_func):
    for numbers in range(number_value_start_func, number_value_end_func):
        is_prime = True
        for number in range(2, (int(numbers / 3) + 1)):
            # for number in range(2, numbers):
            mod_value = numbers % number
            if mod_value == 0:
                is_prime = False
                break
        if is_prime:
            global prime_number_count
            global prime_number_list
            prime_number_list = prime_number_list + "\n" + str(numbers)
            prime_number_count += 1


number_value_start = int(input("Enter the start value : "))

start_position = number_value_start
number_value = int(input("Enter the end value : "))
total_number_check = number_value-start_position
print(f"Total number will be checked : {total_number_check}")
total_thread = 4
segment_number = int(total_number_check / 4)
print(segment_number)
prime_number_count = 0
prime_number_list = ""
# creating thread
number_value_end = number_value_start + segment_number
print(f"t1 start {number_value_start}  end {number_value_end}")
t1 = threading.Thread(target=hunt_prime, args=(number_value_start, number_value_end,))
number_value_start = number_value_end + 1
number_value_end = number_value_end + segment_number
print(f"t2 start {number_value_start}  end {number_value_end}")
t2 = threading.Thread(target=hunt_prime, args=(number_value_start, number_value_end,))
number_value_start = number_value_end + 1
number_value_end = number_value_end + segment_number
print(f"t3 start {number_value_start}  end {number_value_end}")
t3 = threading.Thread(target=hunt_prime, args=(number_value_start, number_value_end,))
number_value_start = number_value_end + 1
number_value_end = number_value
print(f"t4 start {number_value_start}  end {number_value_end}")
t4 = threading.Thread(target=hunt_prime, args=(number_value_start, number_value_end,))
t1.start()
print("Thread1 started")
t2.start()
print("Thread2 started")
t3.start()
print("Thread3 started")
t4.start()
print("Thread4 started")
t1.join()
print("Thread1 end")
t2.join()
print("Thread2 end")
t3.join()
print("Thread3 end")
t4.join()
print("Thread4 end")
print(f"Total prime numbers between {start_position} -{number_value} is {prime_number_count}")
print("--- %s mins ---" % ((time.time() - start_time) / 60))
f = open("prime.txt", "w")
f.write(prime_number_list)
f.close()
print("Data saved in file 'prime.txt'")
