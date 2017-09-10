import itertools
import operator
import reedsolo


def hamming_distance(i1, i2):
    """
    >>> hamming_distance('000', '111')
    3
    >>> hamming_distance('000', '000')
    0
    >>> hamming_distance('000', '010')
    1
    """
    assert len(i1) == len(i2)
    return sum(map(operator.ne, i1, i2))


def hamming_min_distance(l):
    """
    >>> hamming_min_distance(['111', '000', '010'])
    1
    """
    return min(hamming_distance(e1, e2) for e1, e2 in itertools.permutations(l, 2))


def codes(count=16, c_bytes=4):
    r = reedsolo.RSCodec(c_bytes)
    c = [''.join((format(x, '08b') for x in r.encode(chr(i))[1:])) for i in range(count)]
    return c


def bitstring_to_int(s):
    """
    >>> bitstring_to_int('101')
    5
    >>> bitstring_to_int('0')
    0
    >>> bitstring_to_int('1')
    1
    """
    v = 0
    for i, e in enumerate(s):
        if e == '1':
            v += pow(2, len(s) - i - 1)
    return v


def print_enum(c):
    print('enum {')
    for i, v in enumerate(sorted(c)):
        print('    CODE_%02d = 0x%08X,' % (i, v))
    print('};')


def solve():
    """
    >>> solve()
    Get codes with min Hamming distance: 10
    enum {
        CODE_00 = 0x00000000,
        CODE_01 = 0x0F367840,
        CODE_02 = 0x115A88C0,
        CODE_03 = 0x1E6CF080,
        CODE_04 = 0x22B40D9D,
        CODE_05 = 0x2D8275DD,
        CODE_06 = 0x33EE855D,
        CODE_07 = 0x3CD8FD1D,
        CODE_08 = 0x44751A27,
        CODE_09 = 0x4B436267,
        CODE_10 = 0x552F92E7,
        CODE_11 = 0x5A19EAA7,
        CODE_12 = 0x66C117BA,
        CODE_13 = 0x69F76FFA,
        CODE_14 = 0x779B9F7A,
        CODE_15 = 0x78ADE73A,
    };
    """
    c = codes()
    print('Get codes with min Hamming distance:', hamming_min_distance(c))
    int_codes = [bitstring_to_int(x) for x in c]
    print_enum(int_codes)


if __name__ == '__main__':
    solve()
