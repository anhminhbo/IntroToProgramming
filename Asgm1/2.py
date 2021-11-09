# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 1
# Author: Nguyen Cuong Anh Minh (s3931605)
# Created date: 09/11/2021 18:04
# Last modified date: 09/11/2021 18:35

import random
import math

def main():
    print(estimate_pi(1000))


def estimate_pi(N):
    """
    estimate pi of a circle with random points
    :param N: total numbers of random points
    :return: float
    """
    list_of_random_point = generate_n_random_point(N)

    numbers_of_points_inside_circle = count_point_inside_circle(list_of_random_point)

    result = 4 * numbers_of_points_inside_circle/ N

    return result


def generate_n_random_point(N):
    """
    Generate a list with N point with random coordinates
    :param N: total numbers of random points
    :return: list
    """
    # I create a list to hold N points with each point is a list with [x,y] coordinate
    list_of_random_point = []
    for index in range(N):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        random_point_coordinate = [x,y]
        list_of_random_point.append(random_point_coordinate)

    return list_of_random_point

def is_inside_circle(point):
    """
    Check if the input point is inside circle or outside
    :param point: input point coordinate to check
    :return: boolean
    """
    # Calculate the distance to check
    distance = math.sqrt(point[0]**2 + point[1]**2)
    if distance > 1:
        return False
    else:
        return True

def count_point_inside_circle(list_of_random_point):
    """
    count how many points are inside the circle
    :param list_of_random_point:
    :return: integer
    """
    count = 0
    for point in list_of_random_point:
        if is_inside_circle(point):
            count += 1

    return count

main()