from test_framework import generic_test


def swap_bits(x, i, j):
    # TODO - you fill in here.
    
    # Check if the bits at position i, j differ
    if (x>>i & 1) != (x>>j & 1):
        # x^1=0 if x=1 and 0 when x=0
        mask= (1 << i) | (1 << j)
        x = x ^ mask
    
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))
