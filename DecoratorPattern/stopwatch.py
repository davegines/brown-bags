import time


def elapsed_time(fn):
    def wrapper():
        start = time.time()
        fn()
        end = time.time()
        return end - start  # return the elapsed time
    return wrapper
