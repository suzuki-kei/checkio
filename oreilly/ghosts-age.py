#
# https://py.checkio.org/en/mission/ghosts-age/
#

def checkio(opacity):
    ghost_age = 0
    ghost_opacity = 10000
    fibonacci_a = 0
    fibonacci_b = 1
    while ghost_opacity != opacity:
        ghost_age += 1
        while fibonacci_a < ghost_age:
            fibonacci_a, fibonacci_b = fibonacci_b, fibonacci_a + fibonacci_b
        if fibonacci_a == ghost_age:
            ghost_opacity -= ghost_age
        else:
            ghost_opacity += 1
    return ghost_age

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"

