#
# https://py.checkio.org/en/mission/number-radix/
#

from functools import reduce

def checkio(str_number: str, radix: int) -> int:
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:radix]
    figures = tuple(map(digits.find, str_number))

    if -1 in figures:
        return -1
    return reduce(lambda total, figure: total * radix + figure, figures, 0)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A = 10"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

