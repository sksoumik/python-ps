def isAnagram(str1, str2):
    x1 = len(str1)
    x2 = len(str2)

    if x1 != x2:
        return 0

    str1 = sorted(str1)
    str2 = sorted(str2)

    for i in range(0, x1):
        if str1[i] != str2[i]:
            return 0
    return 1


# DRiver code
str1 = "listen"
str2 = "silent"

if isAnagram(str1, str2):
    print("Two strings are anagram")
else:
    print("Two strings are not anagram")
