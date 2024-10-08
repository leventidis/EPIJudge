import functools
import itertools
import random
from typing import Iterator, List

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    binomial_coefficient, check_sequence_is_uniformly_random,
    compute_combination_idx, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook


# Assumption: there are at least k elements in the stream.
def online_random_sample(stream: Iterator[int], k: int) -> List[int]:
    # TODO - you fill in here.
    
    # Store the first k elements of the stream
    result = list(itertools.islice(stream, k))

    num_items_so_far=k
    for val in stream:
        num_items_so_far+=1
        # Generate a random number between [0, num_items_so_far-1], if the number
        # is between [0, k-1] then replace that element with val
        rand_idx = random.randint(0, num_items_so_far-1)
        if rand_idx < k:
            result[rand_idx]=val
    return result


@enable_executor_hook
def online_random_sample_wrapper(executor, stream, k):
    def online_random_sample_runner(executor, stream, k):
        results = executor.run(
            lambda:
            [online_random_sample(iter(stream), k) for _ in range(100000)])

        total_possible_outcomes = binomial_coefficient(len(stream), k)
        stream = sorted(stream)
        comb_to_idx = {
            tuple(compute_combination_idx(stream, len(stream), k, i)): i
            for i in range(binomial_coefficient(len(stream), k))
        }
        return check_sequence_is_uniformly_random(
            [comb_to_idx.get(tuple(sorted(result)), 0) for result in results],
            total_possible_outcomes, 0.01)

    run_func_with_retries(
        functools.partial(online_random_sample_runner, executor, stream, k))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('online_sampling.py',
                                       'online_sampling.tsv',
                                       online_random_sample_wrapper))
