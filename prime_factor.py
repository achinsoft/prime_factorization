import threading
import time


def hunt_prime(number_value_start_func, number_value_end_func):
    for numbers in range(number_value_start_func, number_value_end_func):
        is_prime = True
        for number in range(2, (int(numbers / 2) + 1)):
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
start_time = time.time()
total_number_check = number_value - start_position
print(f"Total number will be checked : {total_number_check}")
total_thread = 12
segment_number = int(total_number_check / total_thread)
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
number_value_end = number_value_end + segment_number
print(f"t4 start {number_value_start}  end {number_value_end}")
t4 = threading.Thread(target=hunt_prime, args=(number_value_start, number_value_end,))
number_value_start = number_value_end + 1
number_value_end = number_value_end + segment_number
print(f"t5 start {number_value_start}  end {number_value_end}")
t5 = threading.Thread(target=hunt_prime, args=(number_value_start, number_value_end,))
number_value_start = number_value_end + 1
number_value_end = number_value_end + segment_number
print(f"t6 start {number_value_start}  end {number_value_end}")
t6 = threading.Thread(target=hunt_prime, args=(number_value_start, number_value_end,))
number_value_start = number_value_end + 1
number_value_end = number_value_end + segment_number
print(f"t7 start {number_value_start}  end {number_value_end}")
t7 = threading.Thread(target=hunt_prime, args=(number_value_start, number_value_end,))
number_value_start = number_value_end + 1
number_value_end = number_value_end + segment_number
print(f"t8 start {number_value_start}  end {number_value_end}")
t8 = threading.Thread(target=hunt_prime, args=(number_value_start, number_value_end,))
number_value_start = number_value_end + 1
number_value_end = number_value_end + segment_number
print(f"t9 start {number_value_start}  end {number_value_end}")
t9 = threading.Thread(target=hunt_prime, args=(number_value_start, number_value_end,))
number_value_start = number_value_end + 1
number_value_end = number_value_end + segment_number
print(f"t10 start {number_value_start}  end {number_value_end}")
t10 = threading.Thread(target=hunt_prime, args=(number_value_start, number_value_end,))
number_value_start = number_value_end + 1
number_value_end = number_value_end + segment_number
print(f"t11 start {number_value_start}  end {number_value_end}")
t11 = threading.Thread(target=hunt_prime, args=(number_value_start, number_value_end,))
number_value_start = number_value_end + 1
number_value_end = number_value
print(f"t12 start {number_value_start}  end {number_value_end}")
t12 = threading.Thread(target=hunt_prime, args=(number_value_start, number_value_end,))

t1.start()
print("Thread1 started")
t2.start()
print("Thread2 started")
t3.start()
print("Thread3 started")
t4.start()
print("Thread4 started")
t5.start()
print("Thread5 started")
t6.start()
print("Thread6 started")
t7.start()
print("Thread7 started")
t8.start()
print("Thread8 started")
t9.start()
print("Thread9 started")
t10.start()
print("Thread10 started")
t11.start()
print("Thread11 started")
t12.start()
print("Thread12 started")
t1.join()
print("Thread1 end")
t2.join()
print("Thread2 end")
t3.join()
print("Thread3 end")
t4.join()
print("Thread4 end")
t5.join()
print("Thread5 end")
t6.join()
print("Thread6 end")
t7.join()
print("Thread7 end")
t8.join()
print("Thread8 end")
t9.join()
print("Thread9 end")
t10.join()
print("Thread10 end")
t11.join()
print("Thread11 end")
t12.join()
print("Thread12 end")
print(f"Total prime numbers between {start_position} - {number_value} is {prime_number_count}")
print("--- %s mins ---" % ((time.time() - start_time) / 60))
f = open("prime.txt", "w")
f.write(prime_number_list)
f.close()
print("Data saved in file 'prime.txt'")
