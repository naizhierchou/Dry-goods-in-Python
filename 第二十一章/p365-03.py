from contextlib import contextmanager
@contextmanager
def my_open(path, mode):
     f = open(path, mode)
     yield f
     f.close()