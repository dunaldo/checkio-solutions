"""FizzBuzz on checkio.org."""


def checkio(x):
    """Checking things."""
    if x % 3 == 0 and x % 5 == 0:
        return "Fizz Buzz"
    elif x % 3 == 0:
        return "Fizz"
    elif x % 5 == 0:
        return "Buzz"
    else:
        return str(x)

l = int(input())
print(checkio(l))
