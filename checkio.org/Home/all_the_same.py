"""Docstring."""
from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    """Main func."""
    return len(set(elements)) <= 1


if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))

    assert all_the_same([]) == True
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
