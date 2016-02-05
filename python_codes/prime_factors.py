"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import math


def initial_value(n):
    i = int(math.sqrt(n))
    for j in range(i, 2, -1):
        if (n % j) == 0:
            for k in range(2, j):
                if (j % k) == 0:
                    break
            else:
                print(j)
                break

if __name__ == '__main__':
    initial_value(600851475143)
