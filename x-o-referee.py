#
# https://py.checkio.org/en/mission/x-o-referee/
#

from typing import List

def checkio(game_result: List[str]) -> str:
    for x in range(3):
        if len({game_result[y][x] for y in range(3)}) == 1:
            if game_result[0][x] in ("X", "O"):
                return game_result[0][x]

    for y in range(3):
        if len({game_result[y][x] for x in range(3)}) == 1:
            if game_result[y][0] in ("X", "O"):
                return game_result[y][0]

    if len({game_result[i][i] for i in range(3)}) == 1:
        if game_result[0][0] in ("X", "O"):
            return game_result[0][0]

    if len({game_result[i][2-i] for i in range(3)}) == 1:
        if game_result[0][2] in ("X", "O"):
            return game_result[0][2]

    return "D"

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

