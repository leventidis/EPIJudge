from typing import List

from test_framework import generic_test


def multiply(num1: List[int], num2: List[int]) -> List[int]:
    # TODO - you fill in here.
    sign = 1
    if (num1[0]<0 and num2[0]>0) or (num1[0]>0 and num2[0]<0):
        sign = -1
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])

    output=[0]*(len(num1)+len(num2))
    for i in range(len(num1)-1, -1, -1):
        for j in range(len(num2)-1, -1, -1):
            val = int(num1[i]) * int(num2[j])
            output[i+j+1]+=val
            output[i+j]+=output[i+j+1]//10
            output[i+j+1]=output[i+j+1]%10

    first_non_zero_idx=-1
    for idx, val in enumerate(output):
        if val != 0:
            first_non_zero_idx=idx
            break

    # All values are zero so return 0
    if first_non_zero_idx<0:
        return [0]
    
    result=output[first_non_zero_idx:]
    result[0]=sign*result[0]
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
