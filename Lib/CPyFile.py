import os


class CPyFile:
    def __init__(self, path):
        self.path = None
        if os.path.exists(path):
            self.path = path
        else:
            raise ValueError('File path is not existed!')

    def read_lines(self, mode="r"):
        r_file = open(self.path, mode=mode)
        lines = r_file.readlines()
        r_file.close()
        return lines
