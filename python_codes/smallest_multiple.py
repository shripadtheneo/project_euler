"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import time

# Number should be multiple of 20 * 19


def smallest_multiple():
    number = 20*19
    count = 2
    while True:
        value = number * count
        counter = 0
        for i in range(2, 21):
            if (value % i) == 0:
                counter += 1

        if counter == 19:
            print(value)
            return

        count += 1


def other_way():
    i = 1
    for k in (range(1, 21)):
        if i % k > 0:
            for j in range(1, 21):
                if (i*j) % k == 0:
                    i *= j
                    break
    print(i)


if __name__ == '__main__':
    start_time = time.time()
    smallest_multiple()
    print("--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    other_way()
    print("--- %s seconds ---" % (time.time() - start_time))

