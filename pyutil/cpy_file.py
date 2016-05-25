import os
import shutil


class CPyFile:
    def __init__(self, path):
        self.path = None
        if os.path.exists(path):
            self.path = path
        else:
            raise ValueError('File path is not existed!')

    def read_lines(self, read_mode="r"):
        if read_mode not in ["r", "rb"]:
            read_mode = "r"
        r_file = self.get_file(read_mode)
        lines = r_file.readlines()
        r_file.close()
        return lines

    def get_file(self, mode="r"):
        return open(self.path, mode=mode)

    def delete_file(self):
        os.remove(self.path)

    def delete_recursive(self):
        shutil.rmtree(self.path)
