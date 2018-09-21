"""Between markers."""


def between_markers(text: str, begin: str, end: str) -> str:
    """Return substring between two given markers."""
    try:
        begin_marker = text.index(begin) + len(begin)
    except ValueError:
        begin_marker = 0
    try:
        end_marker = text.index(end)
    except ValueError:
        end_marker = len(text)

    return (text[begin_marker:end_marker])

if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
