# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 2
# Author: Nguyen Cuong Anh Minh (s3931605)
# Created date: 18/12/2021
# Last modified date: 10:08 18/12/2021

def message_decode(str_list, bin_str):
    """
    Return the string of decoded message
    :param str_list: list of string
    :param bin_str: binary string
    :return: string of decoded message
    """
    # Create the final message to concatenate each time the substring in the list is sorted
    final_message = ""
    # Iterate into each element of str list and bin str to modify the str list elements
    # Sort the str based on number from bin_str
    for index in range(len(str_list)):
        if bin_str[index] == "0":
            str_list[index] = sorted(str_list[index], reverse=False)

        else:
            str_list[index] = sorted(str_list[index], reverse=True)

        # Join the str_list into the final message
        final_message += "".join(str_list[index])

    return final_message
