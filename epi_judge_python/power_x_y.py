from test_framework import generic_test


def power(x: float, y: int) -> float:
    # TODO - you fill in here.
    
    if y==0: return 1

    if y<0:
        x=1.0/x
        y=-1*y

    result = 1
    while y != 0:
        # If 'y' is odd we multiply result with 'x' and reduce 'y' by '1'.
        if y % 2 == 1:
            result *= x
            y -= 1
        # We square 'x' and reduce 'y' by half, x^n => (x^2)^(y/2).
        x *= x
        y //= 2
    return result


if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
