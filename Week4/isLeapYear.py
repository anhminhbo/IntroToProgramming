def is_Leap_Year(year):
    """
    Check if year is Leap or not
    :param year: year to be checked
    :return: boolean
    """
    try:
        if year <= 0:
            raise ValueError('input number should not be less than or equal 0')

        if year % 400 == 0 :
            return True
        if year % 4 == 0 and year % 100 !=0 :
            return True
        else:
            return False
    except Exception as e:
        print(f'There is an error: {e}')

print(is_Leap_Year(1992))
print(is_Leap_Year(2000))
print(is_Leap_Year(1990))
print(is_Leap_Year(2017))