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


def alternate_method():
    """
    a= 2mn; b= m^2 -n^2; c= m^2 + n^2;
    a + b + c = 1000;

    2mn + (m^2 -n^2) + (m^2 + n^2) = 1000;
    2mn + 2m^2 = 1000;
    2m(m+n) = 1000;
    m(m+n) = 500;

    m>n;

    m= 20; n= 5;

    a= 200; b= 375; c= 425;
    :return:
    """
    print 200 * 375 * 425
    return

if __name__ == '__main__':
    pythagorean_triplet()
    alternate_method()
