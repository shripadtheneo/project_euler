# -*- coding: utf-8 -*-
"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def pythagorean_triplet():
    for a in range(997, 0, -1):
        for b in range(997, 0, -1):
            c = 1000 - (a + b)
            if pow(a, 2) + pow(b, 2) == pow(c, 2):
                print a * b * c
                return


if __name__ == '__main__':
    pythagorean_triplet()
