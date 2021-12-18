# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 2
# Author: Nguyen Cuong Anh Minh (s3931605)
# Created date: 18/12/2021
# Last modified date: 11:48 18/12/2021

def shipment_date(product_amount, start_date):
    """
    Return total days needed to ship the product amount
    :param product_amount: the product amount needed to be made
    :param start_date: the first day of working
    :return: total days needed to ship the product amount
    """
    # Create a dict to hold information of the worker including
    # days off and production a day for each one
    worker_dict = {
        'worker_a': {
            "days_off": [0, 2],
            "products_a_day": 8,
        },
        'worker_b': {
            "days_off": [0, 3],
            "products_a_day": 10,
        },
        'worker_c': {
            "days_off": [0, 1, 6],
            "products_a_day": 12,
        }
    }
    # Initialize today , product add up each day and total days to complete the task
    today = start_date
    product_add_up_each_day = 0
    total_days = 0

    # Begin the loop until the product >= product_amount
    while product_add_up_each_day < product_amount:
        for name, prop in worker_dict.items():
            # If today is not the days off of the worker -> add products
            if today not in prop['days_off']:
                product_add_up_each_day += prop['products_a_day']

        # After all the products has been calculated in one day
        # Increment today and set it in range of [0,6] to keep track of current day
        today = (today+1) % 7

        # add total day
        total_days += 1
    return total_days
