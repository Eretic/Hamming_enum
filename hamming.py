import doctest
import itertools
import operator
import reedsolo
import sys


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


def code_generator(count=None, c_bytes=4, c_exp=8):
    i = 0
    r = reedsolo.RSCodec(c_bytes, c_exp=c_exp)
    while i < 2 ** c_exp and (codes is None or i < count):
        yield ''.join((format(x, '0%db' % c_exp) for x in r.encode(bytearray(chr(i), encoding='latin1'))[1:]))
        i += 1


def codes(count=16, c_bytes=4, c_exp=8):
    return [i for i in code_generator(count, c_bytes, c_exp)]


def find_codes_by_distance(min_hamming_distance=14):
    g = code_generator(count=256)
    c = [g.__next__()]
    for el in g:
        if hamming_min_distance(c + [el]) >= min_hamming_distance:
            c += [el]
    return c


def find_codes_by_count(count=16):
    distance = 20
    while True:
        c = find_codes_by_distance(distance)
        if len(c) >= count:
            break
        distance -= 1
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


def print_result(c):
    print('Get %d codes with min Hamming distance:' % len(c), hamming_min_distance(c))
    int_codes = [bitstring_to_int(x) for x in c]
    print_enum(int_codes)


def solve(c_bytes=4, c_exp=8):
    """
    >>> solve()
    Get 16 codes with min Hamming distance: 10
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
    >>> solve(8, 4)
    Get 16 codes with min Hamming distance: 11
    enum {
        CODE_00 = 0x00000000,
        CODE_01 = 0x148172C1,
        CODE_02 = 0x2832E4B2,
        CODE_03 = 0x3CB39673,
        CODE_04 = 0x4364F854,
        CODE_05 = 0x57E58A95,
        CODE_06 = 0x6B561CE6,
        CODE_07 = 0x7FD76E27,
        CODE_08 = 0x86C8D3A8,
        CODE_09 = 0x9249A169,
        CODE_10 = 0xAEFA371A,
        CODE_11 = 0xBA7B45DB,
        CODE_12 = 0xC5AC2BFC,
        CODE_13 = 0xD12D593D,
        CODE_14 = 0xED9ECF4E,
        CODE_15 = 0xF91FBD8F,
    };
    """
    c = codes(c_bytes=c_bytes, c_exp=c_exp)
    print_result(c)


def alternative_solve():
    c = find_codes_by_count(16)
    print_result(c)
    c = find_codes_by_count(8)
    print_result(c)


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        fail, _ = doctest.testmod()
        exit(fail)
    else:
        solve(8, 4)
        alternative_solve()
