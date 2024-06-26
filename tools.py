import os
from time import time
import logging


def decorator_timer(some_function):
    """
    This decorator function measures the execution time of another function.
    It takes a function as input, executes it,
    and returns both the result of the function and the time taken for execution.
    Example: result, execution_time = some_function()
    """
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
            logging.info('The directory is not empty')
            return False
    else:
        logging.info('The directory is not exist')
        return False
