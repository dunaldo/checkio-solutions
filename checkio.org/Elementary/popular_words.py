from collections import Counter

def popular_words(text, words):
    # your code here

    text = dict(Counter(text.replace(',', '').lower().replace('.', '').split()))
    newtext = text.fromkeys(words, 0)
    for key, value in text.items():
        if key in newtext:
            newtext[key] = text[key]
        else:
            continue
    return newtext


if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One,
I had just begun.
When I was Two,
I was nearly new.
''', ['i', 'was', 'three']))

#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert popular_words('''
# When I was One,
# I had just begun.
# When I was Two,
# I was nearly new.
# ''', ['i', 'was', 'three']) == {
#         'i': 4,
#         'was': 3,
#         'three': 0
#     }
#     print("Coding complete? Click 'Check' to earn cool rewards!")
