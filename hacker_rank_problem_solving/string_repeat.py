# https://www.hackerrank.com/challenges/repeated-string/problem


def repeatedString(s, n):
    len_of_string = len(s)
    n_letters = n
    quotient = n_letters // len_of_string
    remainder = n_letters % len_of_string

    # occurance of 'a' in the quotient
    solid_ocr = quotient * (s.count("a"))
    # occurance of 'a' in the remainder
    remainder_ocr = s[:remainder].count("a")
    # add both together and find number of occurance
    n_occ = solid_ocr + remainder_ocr
    return n_occ


if __name__ == "__main__":
    s = input()  # abc
    n = int(input())  # 10
    print(repeatedString(s, n))