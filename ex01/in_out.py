def square(x: int | float) -> int | float:
    """Calculates the square of a number"""
    try:
        result = x ** 2
        return result
    except OverflowError:
        print("Overflow error!")


def pow(x: int | float) -> int | float:
    """Calculates the power of a number"""
    try:
        result = x ** x
        return result
    except OverflowError:
        print("Overflow error!")


def outer(x: int | float, function) -> object:
    """Outer function"""
    count = 0

    def inner() -> float:
        """Inner function"""
        nonlocal x, count
        count += 1
        x = function(x)
        return x
    return inner
