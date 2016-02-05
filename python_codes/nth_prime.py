"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
import math


def nth_prime(n):
    number = 2
    n = 1
    counter = 1
    while n > 0:
        for i in range(math.sqrt(number)):
            if (number % n) != 0:
                number += 1
                break


    return

if __name__ == '__main__':
    nth_prime(10001)
