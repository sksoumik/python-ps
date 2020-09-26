'''
problem url: 
https://www.hackerrank.com/challenges/sock-merchant

''' 
from collections import Counter 

def sockMerchant(n, ar):
    ans = 0
    c = Counter(ar)
    for i in c:
        ans += c[i]//2
    return ans 



if __name__ == "__main__":
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    print(sockMerchant(n, ar))