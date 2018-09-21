"""Digits multiplication."""
from functools import reduce


def checkio(number):
    """Using list comprehasions."""
    return reduce(lambda a, b: a * b if b != 0 else a,
                  [int(x) for x in str(number)])
    # mult = 1
    # numlst = []
    # for i in str(number):
    #     numlst.append(int(i))
    # for i in range(len(numlst)):
    #     if numlst[i] != 0:
    #         mult *= numlst[i]
    # return mult

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
