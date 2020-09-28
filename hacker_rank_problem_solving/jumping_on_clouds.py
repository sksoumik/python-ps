# https://www.hackerrank.com/challenges/jumping-on-the-clouds

def jumpingOnClouds(c):
    # 7
    # 0 0 1 0 0 1 0
    length = len(c)
    n_jumps = 0
    i = 0
    while i < length - 1:
        if i + 2 < length and c[i+2] == 0:
            i = i + 2
            n_jumps += 1
        else:
            i = i + 1
            n_jumps += 1
    return n_jumps
    

if __name__ == "__main__":
    n = int(input())
    jumps = list(map(int, input().strip().split()))
    print(jumpingOnClouds(jumps))
    