#
# https://py.checkio.org/en/mission/boolean-algebra/
#

OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")

def boolean(x, y, operation):
    x = bool(x)
    y = bool(y)

    if operation == "conjunction":
        return int(x and y)
    if operation == "disjunction":
        return int(x or y)
    if operation == "implication":
        return int((not x) or y)
    if operation == "exclusive":
        return int(x != y)
    if operation == "equivalence":
        return int(x == y)
    raise ValueError

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"


