from test_framework import generic_test


def closest_int_same_bit_count(x: int) -> int:
    # TODO - you fill in here.
    
    # Find the smallest bit that next to (right of) the least significant bit and is different to swap them
    for i in range(63):
        if (x>>i)&1 != (x>>(i+1))&1:
            # Swap bit-i with bit-(i+1)
            x ^= ((1<<i) | (1<<(i+1)))
            return x
    return ValueError('All bits are 0 or 1')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('closest_int_same_weight.py',
                                       'closest_int_same_weight.tsv',
                                       closest_int_same_bit_count))
