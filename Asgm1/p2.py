# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 1
# Author: Nguyen Cuong Anh Minh (s3931605)
# Created date: 09/11/2021 18:04
# Last modified date: 09/11/2021 18:35

import random
import math

# def main():
#     print(estimate_pi(1000000))

def estimate_pi(N):
    """
    estimate pi of a circle with random points
    :param N: total numbers of random points
    :return: float
    """
    random_point = generate_n_random_point(N)

    numbers_of_points_inside_circle = count_point_inside_circle(random_point)

    estimated_pi = 4 * numbers_of_points_inside_circle/ N

    return estimated_pi


def generate_n_random_point(numbers_of_points):
    """
    Generate a list with N point with random coordinates
    :param numbers_of_points: total numbers of random points
    :return: list
    """
    # I create a list to hold N points with each point is a list with [x,y] coordinate
    list_random_point = []
    for index in range(numbers_of_points):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        random_point_coordinate = [x,y]
        list_random_point.append(random_point_coordinate)

    return list_random_point

def is_inside_circle(point):
    """
    Check if the input point is inside circle or outside
    :param point: input point coordinate to check
    :return: boolean
    """
    # Calculate the distance to check
    distance = math.sqrt(point[0]**2 + point[1]**2)
    # If distance < 1 mean the point is inside circle
    return distance < 1

def count_point_inside_circle(list_of_random_point):
    """
    count how many points are inside the circle
    :param list_of_random_point: list of random point
    :return: integer
    """
    # if there is point inside circle -> count + 1
    count = 0
    for point in list_of_random_point:
        if is_inside_circle(point):
            count += 1

    return count

# main()