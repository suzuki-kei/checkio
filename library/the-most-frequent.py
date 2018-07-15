#
# https://py.checkio.org/en/mission/the-most-frequent/
#

def most_frequent(data: list) -> str:
    """
        determines the most frequently occurring string in the sequence.
    """
    return sorted(set(data), key=data.count)[-1]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print('Example:')
    print(most_frequent([
        'a', 'b', 'c', 
        'a', 'b',
        'a'
    ]))
    
    assert most_frequent([
        'a', 'b', 'c', 
        'a', 'b',
        'a'
    ]) == 'a'

    assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
    print('Done')

