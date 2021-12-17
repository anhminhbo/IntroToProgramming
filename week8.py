def main():
    # # Question 1
    # print(sort_words_string("without,hello,bag,world"))
    #
    # Question 2
    list1 = generates_two_dimension_array(3,5)
    print(str(list1))

    # # Question 3
    # generate_list()

    # list_of_numbers = [1,2,3,4,5,6,7,8,9,10]
    # # Question 4
    # print(filter_even(list_of_numbers))
    #
    # # Question 5
    # print(square_of_even_number(list_of_numbers))
    #
    # # Question 6
    # print(generate_square_odd_in_list(list_of_numbers))

#-----------Question 1
def sort_words_string(input_string):
    """
    Sorts input string in ascending alphabet
    :param input_string: input string
    :return: string
    """
    string_list_after_split=input_string.split(sep=",")

    string_list_after_split.sort()

    return ",".join(string_list_after_split)

#------------Question 2
def generates_two_dimension_array(x,y):
    """
    Generate two dimension array with given condition
    :param x: input x
    :param y: input y
    :return: list
    """
    result = []
    for row in range(x):
        rowList = []
        for column in range(y):
            rowList.append(row*column)
        result.append(rowList)

    return result

#------------Question 3
def generate_list():
    result_list = []
    for number in range(1,21):
        result_list.append(number**2)

    print(result_list[-1:-6:-1])

#-----------Question 4
def filter_even(list_number):
    return list(filter(is_even,list_number))

def is_even(n):
    if n %2 == 0:
        return True
    else:
        return False

#-----------Question 5
def square_of(n):
    return n**2

def square_of_even_number(list_number):
    return list(map(square_of,filter_even(list_number)))

#-----------Question 6
def generate_square_odd_in_list(list_number):
    result = [number**2 for number in list_number if number%2 != 0]
    return result

main()