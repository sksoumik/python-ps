def tower(n, sourcePole, destinationPole, auxilaryPole):
    # base case
    if (0 == n):
        return
    tower(n - 1, sourcePole, auxilaryPole, destinationPole)
    print("Move the disk", n, "from", sourcePole, "to", destinationPole)
    tower(n - 1, auxilaryPole, destinationPole, sourcePole)


tower(3, 'S', 'D', 'A')
