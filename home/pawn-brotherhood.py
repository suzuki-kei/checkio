#
# https://py.checkio.org/en/mission/pawn-brotherhood/
#

def safe_pawns(pawns: set) -> int:
    def generate_glared_cells(pawns):
        for pawn in pawns:
            x = ord(pawn[0]) - ord("a")
            y = int(pawn[1])
            yield "{}{}".format(chr(x - 1 + ord("a")), y + 1)
            yield "{}{}".format(chr(x + 1 + ord("a")), y + 1)

    glared_cells = set(generate_glared_cells(pawns))
    return len(pawns & glared_cells)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

