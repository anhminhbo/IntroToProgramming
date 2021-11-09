# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 1
# Author: Nguyen Cuong Anh Minh (s3931605)
# Created date: 09/11/2021 18:35
# Last modified date: 09/11/2021 23:14

import math

def main():
   total_flour_in_kg,decision,total_cost = flour_order(10,14,10,10)
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

    money_to_buy_from_A = total_money_to_buy_from_A(total_flour)

    money_to_buy_from_B = total_money_to_buy_from_B(total_flour)

    selected_provider,total_cost = decision_choosed(money_to_buy_from_A,money_to_buy_from_B)

    print(f'We need to order {total_flour}kg of flour, which costs {money_to_buy_from_A}VND if we buy from A and {money_to_buy_from_B}VND if we buy from B.')

    return  total_flour,selected_provider,total_cost

def total_amount_of_flour_in_kg(large_thick, large_thin, medium_thick, medium_thin):
    """
    Return the total flour in kg
    :param large_thick: quantity of large thick pizza
    :param large_thin: quantity of large thin pizza
    :param medium_thick: quantity of medium thick pizza
    :param medium_thin: quantity of medium thin pizza
    :return: integer
    """
    # Total of flour in kg
    total_flour_in_kg = (large_thick * 550 + large_thin * 500 +  medium_thick * 450 + medium_thin * 400)/1000

    # 6% wasted to make pizza
    total_flour_in_kg_with_waste = total_flour_in_kg + 0.06*total_flour_in_kg

    print(total_flour_in_kg_with_waste)

    # Round up to 2kg per order
    actual_total_flour_in_kg= round_up_to_2(total_flour_in_kg_with_waste)

    print(actual_total_flour_in_kg)

    return actual_total_flour_in_kg

def total_money_to_buy_from_A(actual_flour_total_in_kg):
    """
    Return the money if I buy from A
    :param actual_flour_total_in_kg: total amount of flour in kg
    :return: integer
    """
    # Total money = total kg * 30000 VND * discount, convert float to integer
    money_to_buy_from_A = int(actual_flour_total_in_kg * 30000 * discount_from_A(actual_flour_total_in_kg))
    return money_to_buy_from_A

def discount_from_A(actual_flour_total_in_kg):
    """
    Return the discount if I buy from A
    :param actual_flour_total_in_kg: total amount of flour in kg
    :return: float
    """
    # amount <30kg => 3% discount otherwise 5% discount
    if actual_flour_total_in_kg < 30:
        return 0.03
    else:
        return 0.05

def total_money_to_buy_from_B(actual_flour_total_in_kg):
    """
    Return the money if I buy from B
    :param actual_flour_total_in_kg: total amount of flour in kg
    :return: integer
    """
    # Total money = total kg * 31000 VND * discount, convert float to integer
    money_to_buy_from_B = int(actual_flour_total_in_kg * 31000 * discount_from_B(actual_flour_total_in_kg))
    return money_to_buy_from_B

def discount_from_B(actual_flour_total_in_kg):
    """
    Return the discount if I buy from B
    :param actual_flour_total_in_kg: total amount of flour in kg
    :return:
    """
    # amount < 40kg => 5% discount otherwise 10% discount

    if actual_flour_total_in_kg < 40:
        return 0.05
    else:
        return 0.1

def round_up_to_2(total_flour_in_kg_with_waste):
    """
    Return the rounded to 2kg for order amount
    :param total_flour_in_kg_with_waste: total amount of flour in kg
    :return: integer
    """
    # Use math.ceil() to round up
    # For example: 0.1 % 2 = 0,1 => roundUp(0.1 + 1) => 2kg
    # 1.1 % 2 = 1.1 ==> roundUp(1.1) => 2kg
    if total_flour_in_kg_with_waste % 2 > 1:
        actual_total_flour_in_kg = math.ceil(total_flour_in_kg_with_waste)
    else:
        actual_total_flour_in_kg = math.ceil(total_flour_in_kg_with_waste + 1)
    return actual_total_flour_in_kg


def decision_choosed(money_to_buy_from_A,money_to_buy_from_B):
    """
    Return the selected provider and the total cost from that provider
    :param money_to_buy_from_A: total money if I buy from A
    :param money_to_buy_from_B: total money if I buy from B
    :return: string, integer
    """
    # if buy from A > buy from B ==> buy from B otherwise buy from A
    if money_to_buy_from_A > money_to_buy_from_B:
        return "B",money_to_buy_from_B
    else:
        return "A",money_to_buy_from_A

main()