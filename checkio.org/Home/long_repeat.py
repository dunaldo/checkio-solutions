"""Docstring."""


def long_repeat(line):
    """Docstring."""
    try:
        a = line[0]
    except IndexError:
        pass
    longest = 0
    try:
        for i in range(len(line)):
            if line[i] == line[i + 1]:
                    a += line[i + 1]
                    if len(a) > longest:
                        longest = len(a)

            else:
                if len(a) > longest:
                    longest = len(a)
                a = line[i]
    except IndexError:
        pass

    return longest

if __name__ == '__main__':
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
