def mean(args: tuple):
    """Calculates the mean of a list of numbers"""
    result = 0
    for n in args:
        result += n
    return result/len(args)


def median(args: tuple):
    """Calculates the median of a list of numbers"""
    l_args = sorted(args)
    a_len = len(l_args)
    l_middle = int(a_len/2)
    if a_len % 2 == 0:
        return mean((l_args[l_middle], l_args[l_middle - 1]))
    else:
        return l_args[l_middle]


def quartile(args: tuple):
    """Calculates the quartile of a list of numbers"""
    l_args = sorted(args)
    a_len = len(l_args)
    q1 = int(a_len * 0.25)
    q2 = int(a_len * 0.75)
    return [float(l_args[q1]), float(l_args[q2])]


def std(args: tuple):
    """Calculates the standard deviation of a list of numbers"""
    lst = []
    average = mean(args)
    for n in args:
        lst.append((n - average) ** 2)
    return mean(lst) ** 0.5


def var(args: tuple):
    """Calculates the variance of a list of numbers"""
    return std(args) ** 2


def ft_statistics(*args: any, **kwargs: any) -> None:
    """Prints the result of the operations specified in kwargs"""
    op = {
        "mean": mean,
        "median": median,
        "quartile": quartile,
        "std": std,
        "var": var
    }
    op_list = {op[item] for item in kwargs.values() if item in op}
    l_args = [arg for arg in args if isinstance(arg, (int, float))]
    for func in op_list:
        if len(l_args) == 0:
            print('ERROR')
        else:
            print(f'{func.__name__}: {func(l_args)}')
