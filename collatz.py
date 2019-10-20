# the number we will perform the collatz operations on.
n = int(input("enter a positive integer"))

# keep looping until we reach 1.
# Note: this assumes the collatz conjecture is true.
while n != 1:
    #print the current value to n
    print(n)
    #check if n is even
    if n % 2 == 0:
        # if n is even, divide it by two
        n = n // 2
    else:
        # if n is odd, multiply by three and add 1
        n = (3*n) +1

print(n)