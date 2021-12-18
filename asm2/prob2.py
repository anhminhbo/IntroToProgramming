# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 2
# Author: Nguyen Cuong Anh Minh (s3931605)
# Created date: 18/12/2021
# Last modified date: 11:11 18/12/2021

# def main():
#     print(tour_sale({"I": {"luxury": 45, "standard": 26},
#        "Q": {"luxury": 48, "standard": 48},
#        "N": {"luxury": 41, "standard": 18},
#        "J": {"luxury": 9, "standard": 22},
#        "C": {"luxury": 6, "standard": 42},
#        "V": {"luxury": 7, "standard": 35}
#        }))
def tour_sale(sale_dict):
    """
    Return total profit of the company in int, commission dict of each salesperson and best salesperson name
    :param sale_dict:
    :return: total profit of the company in int, commission dict of each salesperson and best salesperson name
    """

    # Calculate total profit
    total_profit = cal_total_profit(sale_dict)

    # commission dict
    commission_dict = commission_of_each_person(sale_dict)

    # Best sale person
    best_salesperson = best_sale_person(commission_dict)

    return total_profit, commission_dict, best_salesperson


def cal_total_profit(this_dict):
    """
    Calculate total profit of the company
    :param this_dict: sale dict
    :return: total profit of the company
    """

    total_profit_company = 0

    # Loop through each key in the dict and calculate the profit based on the type of tour
    for name in this_dict.keys():
        luxury_profit = this_dict[name]['luxury'] * 1000
        standard_profit = this_dict[name]['standard'] * 200
        total_profit_company += luxury_profit + standard_profit

    return total_profit_company


def commission_of_each_person(sale_dictionary):
    """
    commission dict of each sale person
    :param sale_dictionary: sale dict
    :return: a commission dict
    """
    new_dict = {}

    # Loop through each key in the dict and calculate the commission based on the type of tour
    for name in sale_dictionary.keys():
        luxury_commission = sale_dictionary[name]['luxury'] * 1000 * 0.2
        standard_commission = sale_dictionary[name]['standard'] * 200 * 0.1
        total_commission = luxury_commission + standard_commission

        new_dict[name] = total_commission

    return new_dict


def best_sale_person(sale_dict):
    """
    return name of the best sale person
    :param sale_dict: commission diction of each sale person
    :return: name of the best sale person
    """

    max_sale = 0
    best_person_name = ""

    # Loop through the dictionary and find the maximum value and then return the key
    for k, v in sale_dict.items():
        if v > max_sale:
            max_sale = v
            best_person_name = k

    return best_person_name
