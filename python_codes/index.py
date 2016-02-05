import sys


def find_index(input_string):
    length = len(input_string)
    char_dict = {}
    for i in range(length):
        if input_string[i] not in char_dict:
            char_dict[input_string[i]] = 1
        else:
            char_dict[input_string[i]] += 1

    for i in range(length):
        if char_dict[input_string[i]] == 1:
            print(i)
            break


def main():
    input_string = sys.argv[1]
    find_index(input_string)


main()
