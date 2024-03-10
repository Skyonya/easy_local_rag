import pickle
from tools import is_directory_empty, decorator_timer

def process_picklestore(
        data,
        persist_directory,
        silent=True
):
    if is_directory_empty(persist_directory):


def save_pickle(data):
    with open('pickle_store_db/pickle_store.pickle', 'wb') as f:
        pickle.dump(data, f)


def load_pickle():
    with open('pickle_store_db/pickle_store.pickle', 'rb') as f:
        data = pickle.load(f)
    return data
