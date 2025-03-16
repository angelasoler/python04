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
        nonlocal count
        result = 0
        match function.__name__:
            case "square":
                result = 1
                for i in range(2 ** count):
                    result *= function(x)
                count += 1
            case "pow":
                result = function(x)
                for i in range(count):
                    result = function(result)
                count = 2 ** count
            case _:
                try:
                    result = function(x)
                except TypeError:
                    print('Except a function with a number as argument')
        return result
    return inner
