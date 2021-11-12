#Import function is_even from even.py
import even
from even  import *

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

        # if is_even(n):
        #     return False
        # else:
        #     return True
        #
        # return not is_even(n)
        # return not even.is_even()

        return bool(n%2)

    except Exception as e:
       print(f'There is an error: {e}')

print(is_odd(4))