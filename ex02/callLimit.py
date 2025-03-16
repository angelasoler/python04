def callLimit(limit: int):
    """
    Outer function to limit the number
    of times a function can be called
    """
    count = 0

    def callLimiter(function):
        """
        Wrapper function to limit the number of times
        a function can be called
        """
        def limit_function(*args: any, **kwds: any):
            """
            Inner function to limit the number
            of times a function can be called
            """
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(f"Error {function} call too many times")
        return limit_function
    return callLimiter
