import os
from time import time


def decorator_timer(some_function):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = some_function(*args, **kwargs)
        end = time()-t1
        return result, end
    return wrapper


def is_directory_empty(directory):
    if os.path.isdir(directory):
        if not os.listdir(directory):
            return True
        else:
            return False
    else:
        return False
