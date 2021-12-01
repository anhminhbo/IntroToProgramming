# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 1
# Author: Nguyen Cuong Anh Minh (s3931605)
# Created date: 09/11/2021 18:35
# Last modified date: 16/11/2021 18:56

# import math

def main():
   total_flour_in_kg,decision,total_cost = flour_order(1,1,1,10)
   print(total_flour_in_kg)
   print(decision)
   print(total_cost)


def flour_order(large_thick, large_thin, medium_thick, medium_thin):
    """
    Return the total flour I need to order, selected provider be made, and total cost to pay
    :param large_thick: quantity of large thick pizza
    :param large_thin: quantity of large thin pizza
    :param medium_thick: quantity of medium thick pizza
    :param medium_thin: quantity of medium thin pizza
    :return: integer,string,integer
    """
    total_flour = total_amount_of_flour_in_kg(large_thick, large_thin, medium_thick, medium_thin)

    money_to_buy_from_a = total_money_to_buy_from_A(total_flour)

    money_to_buy_from_b = total_money_to_buy_from_B(total_flour)

    selected_provider,total_cost = decision_choosed(money_to_buy_from_a,money_to_buy_from_b)
    # format money ':0' means that width of string is 0 ; ',' to separates each 3 characters with comma and 0f mean that take no float point
    print(f'We need to order {total_flour}kg of flour, which costs {money_to_buy_from_a:0,.0f}VND if we buy from A and {money_to_buy_from_b:0,.0f}VND if we buy from B.')

    return  total_flour,selected_provider,total_cost

def total_amount_of_flour_in_kg(large_thick_quantity, large_thin_quantity, medium_thick_quantity, medium_thin_quantity):
    """
    Return the total flour in kg
    :param large_thick_quantity: quantity of large thick pizza
    :param large_thin_quantity: quantity of large thin pizza
    :param medium_thick_quantity: quantity of medium thick pizza
    :param medium_thin_quantity: quantity of medium thin pizza
    :return: integer
    """
    # Total of flour in kg
    total_flour_in_kg = (large_thick_quantity * 550 + large_thin_quantity * 500 +  medium_thick_quantity * 450 + medium_thin_quantity * 400)/1000


    # 6% wasted to make pizza
    total_flour_in_kg_with_waste = total_flour_in_kg + 0.06*total_flour_in_kg

    # Round up to 2kg per order
    actual_total_flour_in_kg= round_up_to_n(total_flour_in_kg_with_waste,2)


    return actual_total_flour_in_kg

def total_money_to_buy_from_A(flour_total_a):
    """
    Return the money if I buy from A
    :param flour_total_a: total amount of flour in kgr
    :return: integer
    """
    # Total money = total kg * 30000 - total kg * 30000 VND * discount, convert float to integer
    money_buy_a = int((flour_total_a - flour_total_a * discount_from_A(flour_total_a)) * 30000)
    return money_buy_a

def discount_from_A(flour_total_discount_a):
    """
    Return the discount if I buy from A
    :param flour_total_discount_a: total amount of flour in kg
    :return: float
    """
    # amount <30kg => 3% discount otherwise 5% discount

    if flour_total_discount_a < 30:
        return 0.03
    else:
        return 0.05

def total_money_to_buy_from_B(flour_total_b):
    """
    Return the money if I buy from B
    :param flour_total_b: total amount of flour in kg
    :return: integer
    """
    # Total money =total kg * 31000VND -total kg * 31000 VND * discount, convert float to integer
    money_buy_b = int((flour_total_b - flour_total_b * discount_from_B(flour_total_b))  * 31000)
    return money_buy_b

def discount_from_B(flour_total_discount_b):
    """
    Return the discount if I buy from B
    :param flour_total_discount_b: total amount of flour in kg
    :return: float
    """
    # amount < 40kg => 5% discount otherwise 10% discount

    if flour_total_discount_b < 40:
        return 0.05
    else:
        return 0.1

def round_up_to_n(flour_ord,n):
    """
    Return the rounded to n kg for order amount
    :param flour_ord: total amount of flour in kg
    :param n: kg to round up to
    :return: integer
    """
    # # Use math.ceil() to round up
    # # For example: 0.1 % 2 = 0,1 => roundUp(0.1 + 1) => 2kg
    # # 1.1 % 2 = 1.1 ==> roundUp(1.1) => 2kg
    # if flour_ord % 2 > 1:
    #     flour_formatted = math.ceil(flour_ord)
    # else:
    #     flour_formatted = math.ceil(flour_ord + 1)
    # return flour_formatted

    # Second approach
    # if flour order % n == 0 ==> return flour order
    # else return flour order + n - flour_ord % n
    if flour_ord % n != 0:
        remainder = flour_ord % n
        diff_from_original_to_round = n - remainder
        return int(flour_ord + diff_from_original_to_round)
    return flour_ord



def decision_choosed(money_from_a,money_from_b):
    """
    Return the selected provider and the total cost from that provider
    :param money_from_a: total money if I buy from A
    :param money_from_b: total money if I buy from B
    :return: string, integer
    """
    # if buy from A > buy from B ==> buy from B otherwise buy from A
    if money_from_a > money_from_b:
        return "B",money_from_b
    else:
        return "A",money_from_a

main()