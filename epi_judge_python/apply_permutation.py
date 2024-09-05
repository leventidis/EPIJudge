from typing import List

from test_framework import generic_test


def apply_permutation(perm: List[int], A: List[int]) -> None:
    # TODO - you fill in here.
    for i in range(len(A)):
        # check if the element at index i has not been moved by checking if perm[i] is non-negative
        next=i
        while perm[next]>=0:
            A[i], A[perm[next]] = A[perm[next]], A[i]
            tmp=perm[next]
            perm[next]-=len(perm)
            next=tmp
    
    # Restore perm
    perm = [a + len(perm) for a in perm]
    return


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('apply_permutation.py',
                                       'apply_permutation.tsv',
                                       apply_permutation_wrapper))
