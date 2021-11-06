#Import function is_even from even.py
from even import *

def is_odd(n):
    """
    Check if n is odd
    :param: n: the integer number that needed to be checked
    :return: boolean
    """
    try:
        if n <= 0:
            raise ValueError('input number should not be less than or equal 0')
        # if n % 2 != 0:
        #     return True
        # else:
        #     return False
        if is_even(n):
            return False
        else:
            return True

    except Exception as e:
       print(f'There is an error: {e}')

print(is_odd(4))