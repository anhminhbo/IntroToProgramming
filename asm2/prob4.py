# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 2
# Author: Nguyen Cuong Anh Minh (s3931605)
# Created date: 18/12/2021
# Last modified date: 23:45 18/12/2021

def encode_str(s):
    """
    return the encoded string
    :param s: input string
    :return: encoded string
    """
    # initialize encoded string and new list to hold value after convert string to ord() and then do the reverse
    new_list_after_converse_to_ord_and_reverse = []

    # Loop through each character in input string and do the conversion
    # ord() return int so have to convert back using str() and do [::-1] to reverse the string
    for char in s:
        new_list_after_converse_to_ord_and_reverse.append(str(ord(char))[::-1])

    # Even position in original string in reality actually is odd position in computing
    # and vice versa

    # Loop through each value in the list
    # if the index is odd, loop through that value str to modified it
    # by adding 1 to even position num character
    for index_lst in range(len(new_list_after_converse_to_ord_and_reverse)):
        if index_lst % 2 != 0:
            # Initialize new string to hold new modified value and then we will assigned it back to the list
            new_num_str = ""
            # Loop through each character in the string
            for index_str in range(len(new_list_after_converse_to_ord_and_reverse[index_lst])):
                # if the index is even take (int + 1)%10 to convert to [0,9] and convert back to str
                # otherwise just concatenate to new string
                if index_str % 2 == 0:
                    new_num_str += str((int(new_list_after_converse_to_ord_and_reverse[index_lst][index_str]) + 1) % 10)
                else:
                    new_num_str += new_list_after_converse_to_ord_and_reverse[index_lst][index_str]
            # After finish the loop, modified the value in the list with the new string
            new_list_after_converse_to_ord_and_reverse[index_lst] = new_num_str

    # Join the complete modified list into string
    encoded_s = ''.join(new_list_after_converse_to_ord_and_reverse)

    return encoded_s
