#
# https://py.checkio.org/en/mission/feed-pigeons/
#

def checkio(number):
    def pigeons(n):
        return n * (n + 1) / 2

    for i in range(number + 1):
        number -= pigeons(i - 1)
        if number <= 0:
            return pigeons(i - 1)
        number -= i
        if number <= 0:
            return pigeons(i - 1) + (number + i)
    return 0

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"

