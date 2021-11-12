def main():
    """
    Program to print out the pattern base on n integer
    :return:
    """
    try:
        inputNumber = int(input("input your number: "))

        if inputNumber <= 0:
            raise TypeError("input number should not be less than or equal 0")

        print_Pattern_based_on(inputNumber)
    except Exception as e:
        print(f'There is an error: {e}')


def print_Pattern_based_on(n):
    """
    Print Pattern based on n integer
    :param n: input integer to print pattern based on
    :return: none
    """
    # Through given example, we create a nxn table to print each elements
    # n integer = n rows; n columns => Nested loop

    #First approach
    # with first loop to loop through each rows
    # we use range() so should be range(1,n+1) to loop from row 1 to row n.
    # for row in range(1,n+1):
    #     # Second loop through each column to fill in element
    #     # 1st row: fill n elements
    #     # 2nd row: fill n - 1 elements
    #     # => formula for each row is print (n - column + 1) elements => loop from 1 to (n - row +1)
    #     for column in range(1,n- row + 2): # range() so the end have to plus 1
    #         print(column,end=" ")
    #
    #     #After finish fill elements in a row, move cursor to a new row
    #     print()
    #

    #Second approach
    # Go backward to set indexRow from n to 1
    for indexRow in range(n,0,-1):
        #for first row print indexRow elements
        for indexColumn in range(1, indexRow + 1):
            print(indexColumn, end=" ")
        print()


main()