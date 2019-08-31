def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    return (a * b) / gcd(a, b)


a = int(input())
b = int(input())

print("gcd", gcd(a, b))
print("lcm", lcm(a, b))
