"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers
is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def largest_palindrome():
    prev_product = 0
    new_i = 0
    new_j = 0
    for i in range(999, 100, -1):
        for j in range(999, 100, -1):
            if new_i < i or new_j < j:
                product = i * j

                if str(product) == str(product)[::-1]:
                    if prev_product < product:
                        prev_product = product
                        new_i = i
                        new_j = j
    print(prev_product)

largest_palindrome()
