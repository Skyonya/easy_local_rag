import os
from time import time
import logging


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
            logging.info('The directory is not empty')
            return False
    else:
        logging.info('The directory is not exist')
        return False
