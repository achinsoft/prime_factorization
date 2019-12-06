from multiprocessing import Process, Queue
import time


def hunt_prime(number_to_check):
    is_prime = True
    for number in range(2, (int(number_to_check / 2) + 1)):
        # for number in range(2, numbers):
        mod_value = number_to_check % number
        if mod_value == 0:
            is_prime = False
            break
    if is_prime:
        f1 = open("prime.txt", "a")
        f1.write(str(number_to_check) + "\n")
        f1.close()


if __name__ == '__main__':
    f = open("prime.txt", "w")
    f.close()
    number_value_start = int(input("Enter the start value : "))
    if number_value_start < 2:
        print("Invalid data..Auto Set to Default value")
        number_value_start = 2
    start_position = number_value_start
    number_value = int(input("Enter the end value : "))
    if number_value < number_value_start:
        print("Invalid data..Auto Set to Default value")
        number_value = number_value_start + 1
    start_time = time.time()
    total_number_check = number_value - start_position
    print(f"Total number will be checked : {total_number_check}")
    total_thread = 4
    print(f"Total thread {total_thread}")
    t1 = Process(target=hunt_prime, args=(number_value_start,))