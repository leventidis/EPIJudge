from test_framework import generic_test

# Similar to Leetcode
def parity(x: int) -> int:
    # Count number of 1 bits
    num_1_bits=0
    while x:
        num_1_bits+=1
        x=x&(x-1)

    return num_1_bits%2


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
