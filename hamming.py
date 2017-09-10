import itertools
import operator
import pprint
import reedsolo


def hamming_distance(i1, i2):
    assert len(i1) == len(i2)
    return sum(map(operator.ne, i1, i2))


def hamming_min_distance(l):
    return min(hamming_distance(e1, e2) for e1, e2 in itertools.permutations(l, 2))


def codes(count=16, c_bytes=4):
    r = reedsolo.RSCodec(c_bytes)
    c = [''.join((format(x, '08b') for x in r.encode(chr(i))[1:])) for i in range(count)]
    return c


def bitstring_to_int(s):
    v = 0
    for i, e in enumerate(s):
        if e == '1':
            v += pow(2, len(s) - i - 1)
    return v


def print_enum(c):
    print('enum {')
    for i, v in enumerate(sorted(c)):
        print('\t CODE_%02d = 0x%08X,' % (i, v))
    print('};')


def solve():
    c = codes()
    print('Get codes with min Hamming distance:', hamming_min_distance(c))
    int_codes = [bitstring_to_int(x) for x in c]
    print_enum(int_codes)


if __name__ == '__main__':
    solve()
