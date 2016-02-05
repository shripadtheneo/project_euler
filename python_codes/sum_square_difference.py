"""
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

(1 + 2 + ... + n)^2 = n^2 * (n+1)^2 * 1/4

1^2 + 2^2 + ... + n^2 = n * (n+1) * (2n+1) * 1/6

Thus easily applicable to any n.

"""


def sum_square_difference():
    sum_of_square = 1
    for i in range(2, 101):
        sum_of_square += i**2
    total = 1
    for i in range(2, 101):
        total += i
    square_of_sum = total**2

    print(square_of_sum - sum_of_square)
    return


if __name__ == '__main__':
    sum_square_difference()