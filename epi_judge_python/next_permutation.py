from typing import List

from test_framework import generic_test


def next_permutation(perm: List[int]) -> List[int]:
    # TODO - you fill in here.
    
    # Find Pivot
    pivot=len(perm)-2
    while pivot>=0 and perm[pivot]>=perm[pivot+1]:
        pivot-=1
    
    if pivot<0:
        return []
    
    # Find smallest value after pivot that is greater than perm[pivot] and swap
    for i in range(len(perm)-1, pivot, -1):
        if perm[i]>perm[pivot]:
            perm[pivot], perm[i] = perm[i], perm[pivot]
            break
    
    # Reverse the values in perm after pivot
    perm[pivot+1:]=reversed(perm[pivot+1:])

    return perm


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('next_permutation.py',
                                       'next_permutation.tsv',
                                       next_permutation))
