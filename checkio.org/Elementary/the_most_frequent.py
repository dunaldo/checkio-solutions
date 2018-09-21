"""The Most Frequent."""


def most_frequent(data):
    """Determine the most frequently occurring string in the sequence."""
    somedict = {key: data.count(key) for key in data}
    return sorted(somedict.items(), key=lambda item: item[1],
                  reverse=True)[0][0]
    """This is how you SHOULD solve it."""
    # return max(data, key=data.count)

if __name__ == '__main__':
    """These "asserts" using only for self-checking and not necessary
    for auto-testing"""
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
