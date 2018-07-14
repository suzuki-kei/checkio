#
# https://py.checkio.org/en/mission/long-repeat/
#

def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    previous = None
    run_length = 0
    max_run_length = 0

    for i in range(len(line)):
        if line[i] == previous:
            run_length += 1
        else:
            previous = line[i]
            run_length = 1
        if run_length > max_run_length:
            max_run_length = run_length
    return max_run_length

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')

