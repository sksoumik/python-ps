# Fizbuzz problem: n is the user input (integer) and from 1 to n, if
# any number is divisible by 3 then replace it with Fizz, if any number is divisible by 5 then,
# replace it with Buzz, if it is divisible by both, then replace it with FizzBuzz, else replace
# the other numbers.
def FizzBuzz(num):
    for i in range(1, num + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")


FizzBuzz(int(input()))
