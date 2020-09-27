# https://www.hackerrank.com/challenges/counting-valleys 

def counting_valleys(n, steps):
    sea_lavel = valley = 0

    for step in steps:
        if step == 'U':
            sea_lavel += 1
        else:
            sea_lavel -= 1

        if step == 'U' and sea_lavel == 0:
            valley += 1

    return valley


if __name__ == "__main__":
    n = int(input())
    steps = input()

    num_valleys = counting_valleys(n, steps)
    print(num_valleys)
