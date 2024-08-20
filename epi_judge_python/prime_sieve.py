from typing import List

from test_framework import generic_test
import math

# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    # TODO - you fill in here.
    if n<2:
        return []
    
    is_prime=[True]*(n+1)
    is_prime[0]=False
    is_prime[1]=False
    upper_bound=math.ceil(math.sqrt(n))+1
    for i in range(2, upper_bound):
        if is_prime[i]:
            # Set all multiples if i to False since they cannot be primes
            # We start from i*i since every number that is not a prime less than i*i will have a largest prime factor less than i            
            for multiple in range(i*i, n+1, i):
                is_prime[multiple]=False

    return [i for i in range(len(is_prime)) if is_prime[i]==True]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
