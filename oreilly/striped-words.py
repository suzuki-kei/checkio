#
# https://py.checkio.org/en/mission/striped-words/
#

import re

VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"

def checkio(text):
    striped_word_pattern = re.compile(
        "(^([{v}][{c}])+[{v}]?)$|(^([{c}][{v}])+[{c}]?$)".format(v=VOWELS, c=CONSONANTS),
        re.IGNORECASE)
    words = re.split("[ ,.?]", text)
    return len(list(filter(striped_word_pattern.match, words)))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"

