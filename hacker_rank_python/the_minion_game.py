def minion_game(string):
    vowels = set('AEIOU')
    stuart = kevin = 0

    for i, value in enumerate(string):
        if value in vowels:
            kevin += len(string) - i
        else:
            stuart += len(string) - i

    if kevin > stuart:
        print("Kevin {}".format(kevin))
    elif stuart > kevin:
        print("Stuart {}".format(stuart))
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)




