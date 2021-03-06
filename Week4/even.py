def is_even(n):
    """
    Check if n is even
    :param: n: the integer number that needed to be checked
    :return: boolean
    """
    try:
        if n <= 0:
            raise ValueError('input number should not be less than or equal 0')
        return n % 2 == 0
    except Exception as e:
       print(f'There is an error: {e}')
