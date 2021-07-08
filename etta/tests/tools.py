import os
import errno
import traceback

def silent_remove(filename):
    """Remove file if it exists.
    Source: https://stackoverflow.com/a/10840586

    Args:
        filename (path-like): path of file to remove
    """
    try:
        os.remove(filename)
    except OSError as e:  # this would be "except OSError, e:" before Python 2.6
        if e.errno != errno.ENOENT:  # errno.ENOENT = no such file or directory
            raise  # re-raise exception if a different error occurred


class FileCheck(object):
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        silent_remove(self.filename)
        return self

    def __exit__(self, exc_type, exc_value, tb):
        if exc_type is not None:
            traceback.print_exception(exc_type, exc_value, tb)
            return False
        assert os.path.isfile(self.filename), f'results file {self.filename} does not exist'
        assert os.path.getsize(self.filename) != 0, f'results file {self.filename} is empty'
        silent_remove(self.filename)
    
    def check_min_length(self, min_length):
        with open(self.filename, 'r') as f:
            assert len(f.readlines()) >= min_length, f'results file {self.filename} is too short'
