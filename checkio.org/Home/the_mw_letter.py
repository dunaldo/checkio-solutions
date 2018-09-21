"""The Most Wanted Letter."""
import re


def checkio(text):
    """Docstring."""
    text = re.sub(r'[^a-zA-Z]', '', text)
    # print(text)
    text = sorted(text.lower())
    # print(sorted(text))
    # storage = {}
    # storage = {key: text.count(key) for key in sorted(text)}
    # return sorted({key: text.count(key) for key in sorted(text)}.items(),
    #               key=lambda item: item[1], reverse=True)[0][0]
    return max(text, key=text.count)

if __name__ == '__main__':
    """These "asserts" using only for self-checking and
    not necessary for auto-testing"""
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
