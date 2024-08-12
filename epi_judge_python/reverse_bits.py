from test_framework import generic_test


def reverse_bits(x: int) -> int:
    # TODO - you fill in here.
    
    result=0
    for i in range(64):
        bit = (x >> i) & 1
        if bit:
            result += (bit << (63-i))

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
