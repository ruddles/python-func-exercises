# Fill out the implementation of the logger
# to return a function that:
# - prints out the name of the func and the arguments
# - calls func with the arguments
# - prints out the name of the function and the result
# - returns the result

def logger(func):
    def logging_function(*args):
        print(f"calling {func.__name__} with args {args}")
        result = func(*args)
        print(f"result of {func.__name__} is {result}")
        return result

    return logging_function


def add(x, y):
    return x+y


def subtract(x, y):
    return x-y


# Set up add and subtract loggers
logging_add = logger(add)
logging_subtract = logger(subtract)

logging_add(2, 3)
logging_subtract(4, 10)
