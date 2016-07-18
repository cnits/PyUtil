class CPyEncodingConverter:
    def __init__(self, value):
        self.value = value
        pass

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
