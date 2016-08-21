from itertools import islice

def to_binary(val):
    return bin(val)


def to_ascii(val):
    return ord(str(val))


def to_character(val, is_unicode=True):
    if is_unicode is True:
        return unichr(val)
    else:
        return chr(val)


def to_octal(val):
    return oct(val)


def to_hexadecimal(val):
    return hex(val)


def from_bin_to_str(val):
    s = ""
    data = str(val).split(" ")
    for i in data:
        s += chr(int(i, 2))
    return s


def from_str_to_bin(val):
    b = ""
    for i in val:
        b += " " + str(bin(ord(i))).lstrip("0b")
    return b

def get_chunks(ls, sz):
    return [ls[i:i + sz] for i in range(0, len(ls), sz)]


def get_chunks2(ls, sz):
    it = iter(ls)
    return list(iter(lambda: tuple(islice(it, sz)), ()))
