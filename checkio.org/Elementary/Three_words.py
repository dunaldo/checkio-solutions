"""Three Words."""


def checkio(words):
    """Great use of map."""
    return 3 * 'True' in ''.join(map(str, (map(str.isalpha, words.split()))))

# def checkio(words):
#     """Docstring."""
#     alphacounter = 0
#     for i in words.split():
#         if i.isalpha():
#             alphacounter += 1
#             if alphacounter >= 3:
#                 return True
#         else:
#             alphacounter = 0
#     return False

# These "asserts" using only for self-checking and not necessary
# for auto-testing

if __name__ == '__main__':
    assert checkio("Hello World hello") is True, "Hello"
    assert checkio("He is 123 man") is False, "123 man"
    assert checkio("1 2 3 4") is False, "Digits"
    assert checkio("bla bla bla bla") is True, "Bla Bla"
    assert checkio("Hi") is False, "Hi"
    print("Done")
