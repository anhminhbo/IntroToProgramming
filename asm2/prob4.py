# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 2
# Author: Nguyen Cuong Anh Minh (s3931605)
# Created date: 18/12/2021
# Last modified date: 17:00 18/12/2021

def encode_str(s):
    """
    return the encoded string
    :param s: input string
    :return: encoded string
    """
    # initialize encoded string and new string after convert to ord() and then do the reverse
    encoded_s = ""

    new_string_after_converse_to_ord_and_reverse = ""

    # Loop through each character in input string and do the conversion
    # ord() return int so have to convert back using str() and do [::-1] to reverse the string
    for char in s:
        new_string_after_converse_to_ord_and_reverse += str(ord(char))[::-1]

    # Loop through each character in the string
    # if the index is even, convert the character to int to do calculation, + 1 and then % 10 to
    # make the value [0,9] and then convert back to str and concatenated into the encoded_s
    # otherwise concatenate the character at the position
    for index in range(len(new_string_after_converse_to_ord_and_reverse)):
        if index % 2 == 0:
            encoded_s += str((int(new_string_after_converse_to_ord_and_reverse[index]) + 1) % 10)
        else:
            encoded_s += new_string_after_converse_to_ord_and_reverse[index]
    return encoded_s
