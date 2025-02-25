def check(func):
    def wrapper(a, b):
        if b == 0:
            return "Denominator cannot be zero.."
        return func(a, b)
    return wrapper


@check
def divide(a, b):
    return a / b


print(divide(5, 2))














