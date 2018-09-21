"""House Password."""


def checkio(data):
    """Main function."""
    return (len(data) > 9 and
            True in [i.isdigit() for i in data] and
            True in [i.isalpha() for i in data] and
            True in [i.isupper() for i in data] and
            True in [i.islower() for i in data])

if __name__ == '__main__':
    '''These "asserts" using only for self-checking and not necessary
    for auto-testing'''
    assert checkio('A1213pokl') is False, "1st example"
    assert checkio('bAse730onE4') is True, "2nd example"
    assert checkio('asasasasasasasaas') is False, "3rd example"
    assert checkio('QWERTYqwerty') is False, "4th example"
    assert checkio('123456123456') is False, "5th example"
    assert checkio('QwErTy911poqqqq') is True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn"
          "cool rewards!")
