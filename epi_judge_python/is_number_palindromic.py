from test_framework import generic_test


def is_palindrome_number(x: int) -> bool:
    # TODO - you fill in here.
    # If the last digit is 0 then in order to be palindrome x must be 0
    if x<0 or (x%10==0 and x!=0):
        return False
    
    reverse_num = 0
    while x > reverse_num:
        reverse_num = reverse_num * 10 + x%10
        x //= 10

    # When the length is an odd number then the middle digit can be removed by doing integer division with 10
    return x==reverse_num or x == reverse_num//10 

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
