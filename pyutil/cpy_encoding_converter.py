class CPyEncodingConverter:
    def __init__(self, value):
        self.value = value

    def to_binary(self):
        return bin(self.value)

    def to_ascii(self):
        return ord(str(self.value))

    def to_character(self, is_unicode=True):
        if is_unicode is True:
            return unichr(self.value)
        else:
            return chr(self.value)

    def to_octal(self):
        return oct(self.value)

    def to_hexadecimal(self):
        return hex(self.value)

    def from_bin_to_str(self):
        s = ""
        data = str(self.value).split(" ")
        for i in data:
            s += chr(int(i, 2))
        return s

    def from_str_to_bin(self):
        b = ""
        for i in self.value:
            b += " " + str(bin(ord(i))).lstrip("0b")
        return b
