# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 1
# Author: Nguyen Cuong Anh Minh (s3931605)
# Created date: 09/11/2021 17:30
# Last modified date: 09/11/2021 18:03

import random

def main():
    integer_list = generateRandomList(20)
    print(integer_list)
    print(find_split_80(integer_list))

# For Question 1: find a number in list of 20 numbers where exactly 80% of numbers in lists
# are equal to or smaller than it ==> 80% of the list is 0.8 * 20 = 16
# Solution: sort the input array in ascending order and output the value at index 16 of the array
# because the 17th value in 20 integers in ascending order qualifies the condition
def find_split_80(integer_list):
    """
    This function return the number that satisfies the condition
    :param integer_list: input integer list
    :return: integer
    """
    # sort the input integer list
    integer_list.sort()
    print(integer_list)

    split_80 = integer_list[16]

    return split_80

def generateRandomList(n):
    """
    generate random list for test cases
    :param n: length of the list
    :return:
    """
    integer_list = []
    for index in range(n):
       integer_list.append(random.randint(0,100))
    return integer_list

main()