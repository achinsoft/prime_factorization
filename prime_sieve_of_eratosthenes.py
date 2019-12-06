import time

master_number_list = []
default_prime_number = 0
number_value_start = int(input("Enter the start value : "))

if number_value_start < 2:
    print("Invalid data..Auto Set to Default value")
    number_value_start = 3
    default_prime_number = 2
    master_number_list.append(default_prime_number)
elif number_value_start % 2 == 0:
    number_value_start = number_value_start + 1
else:
    number_value_start = number_value_start

number_value_end = int(input("Enter the end value : "))
number_value_end = number_value_end + 1
if number_value_end < number_value_start:
    print("Invalid data..Auto Set to Default value")
    number_value_end = number_value_start + 1

total_number_check = number_value_end - number_value_start
print(f"Total number will be checked : {total_number_check}")
start_time = time.time()

segment_time_start = time.time()
for p in range(number_value_start, number_value_end, 2):
    master_number_list.append(p)

print(f"Time to create list {time.time() - segment_time_start}")
for p in range(number_value_start, number_value_end, 2):
    if p * p > number_value_end:
        print(f"Break at {p} saving calculation for {number_value_end-p}")
        break
    for n in range(p, number_value_end, 2):
        if n*p in master_number_list:
            master_number_list.remove(n*p)

print(master_number_list)

print(f"Total prime numbers between {number_value_start} - {number_value_end} is {len(master_number_list)}")
print("--- %s mins ---" % ((time.time() - start_time) / 60))
f = open("prime.txt", "w")
for prime_number in master_number_list:
    f.write(str(prime_number)+"\t")
f.writelines("\n--- %s mins ---" % ((time.time() - start_time) / 60))
f.close()
print("Data saved in file 'prime.txt'")
