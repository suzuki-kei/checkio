#
# https://py.checkio.org/en/mission/three-words/
#

import re

def checkio(words: str) -> bool:
    return bool(re.search(r"[a-zA-Z]+ [a-zA-Z]+ [a-zA-Z]+", words))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

