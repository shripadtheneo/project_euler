# -*- coding: utf-8 -*-
"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
chain_dict = {}


def even_detected(number):
    new_number = number / 2
    return new_number


def odd_detected(number):
    new_number = (3 * number) + 1
    return new_number


def chain_creation(original_number):
    chain = [original_number]
    number = original_number
    while number != 1:
        if number % 2 == 0:
            number = even_detected(number)
            chain.append(number)
        else:
            number = odd_detected(number)
            chain.append(number)

    chain_dict[original_number] = chain


def longest_chain():
    max_length = 0
    max_key = 0
    for key, value in chain_dict.items():
        length = len(value)
        if max_length < length:
            max_length = length
            max_key = key
    print max_key, max_length

if __name__ == '__main__':
    for i in range(1, 101):
        chain_creation(original_number=i)

    longest_chain()
