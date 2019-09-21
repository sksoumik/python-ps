"""
https://www.hackerrank.com/challenges/find-a-string
"""


def count_substring(string, sub_string):
    l1 = len(string)
    l2 = len(sub_string)
    count = 0
    for i in range(l1 - l2 + 1):
        if sub_string == string[i: i + l2]:
            count = count + 1

    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
