import time


def SieveOfEratosthenes(n):
    # Create a boolean array "prime[0..n]" and
    # initialize all entries it as true. A value  
    # in prime[i] will finally be false if i is 
    # Not a prime, else true. 
    prime = [True for i in range(n + 1)]

    p = 2
    while (p * p <= n):

        # If prime[p] is not changed, then it is  
        # a prime
        if (prime[p] == True):

            # Update all multiples of p 
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    c = 0
    f = open("prime.txt", "w")
    # Print all prime numbers 
    for p in range(2, n):
        if prime[p]:
          #  print(p)
            f.write(str(p) + "\t")
            c += 1
    f.close()
    return c


# Driver function
t0 = time.time()
c = SieveOfEratosthenes(100)
print("Total prime numbers in range:", c)

t1 = time.time()
print("Time required:", t1 - t0) 