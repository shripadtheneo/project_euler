"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2,
the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of
the even-valued terms.
"""


def fibonacci_series(n):
    i = 0
    j = 1
    next_value = 0
    total = 0
    while next_value < n:
        next_value = i + j
        if next_value < n:
            if not (next_value % 2):
                total += next_value
        else:
            break
        i = j
        j = next_value
    print(total)

if __name__ == '__main__':
    fibonacci_series(4000000)
