def main():
    """
    Run the program to print all the prime number that is less than the input number
    :return:
    """
    try:
        inputNumber = int(input("input your number: "))

        print("the prime numberd less than",inputNumber,"is/are:")
        # loop from 0 to inputNumber to find all the prime number
        for number in range(inputNumber):
            if is_prime(number):
                print(number)
    except Exception as e:
        print(f'There is an error: {e}')

def is_prime(number):
    """
    Check if the number is Prime or not
    :param number: number to be checked
    :return: boolean
    """
    # Handle special case when number <= 1
    if number <= 1:
        return False
    # Handle special case when number = 2
    if number == 2:
        return True

    # Prime Number only divided by 1 and itself so
    # Iterate each number from 2 to inputNumber to check if any is divided by inputNumber
    for i in range(2,number):
        if number % i == 0:
            return False

    return True


main()