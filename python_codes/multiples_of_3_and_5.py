"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""


def alternate():
    n = 0
    data = 0
    while n < 1000:
        if not (n % 3) or not (n % 5):
            data += n
        n += 1

    print(data)

if __name__ == '__main__':
    alternate()
