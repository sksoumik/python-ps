"""
https://www.hackerrank.com/challenges/python-mutations
"""


# Method 1
def mutate_string(string, position, character):
    string = string[:position] + character + string[position + 1:]
    return string


# Method 2
def mutate_string_method2(string, position, character):
    l = list(string)
    l[position] = character
    string = ''.join(l)
    return string


#
# if __name__ == '__main__':
#     s = input()
#     i, c = input().split()
#     s_new = mutate_string(s, int(i), c)
#     print(s_new)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string_method2(s, int(i), c)
    print(s_new)
