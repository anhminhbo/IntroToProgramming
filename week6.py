def main():
    """
    Week 6 function running here
    :return: none
    """

    # question1()

    # question2()

    # question3()

    homework()
#------------Question 1
def harmonic(n):
    """
    calculate value of harmonic series of n
    :param n: precison parameter to calculate value of harmonic series
    :return: float
    """
    # f(n) = 1 + 1/2 + 1/3 +...+ 1/(n-1) + 1/n
    # f(n-1) = 1 + 1/2 + 1/3 +...+ 1/(n-1)
    # => f(n) = 1/n + f(n-1)
    if n==1:
        return float(1)
    else:
        return 1/n + harmonic(n-1)

    # Iteration
    # sum = 0
    # for number in range(1,n+1):
    #     sum += 1/number
    # return sum

def format_float_2decimals(floatNumber):
    """
    format float to 2 decimals behind
    :param floatNumber: number to be format
    :return: none
    """
    float_formatter_2decimals = "{:.2f}"
    print(f'{float_formatter_2decimals.format(harmonic(floatNumber))}')

def question1():
    """
    Test cases for question 1
    :return: none
    """
    testCases = [3,1,5]
    for testCase in testCases:
        print("for testcase:",testCase,"the result is")
        format_float_2decimals(testCase)
        print("----------")


# --------------------Question 2
def print_triangular_numbers(n):
    """
    Print out n triangular numbers
    :param n: mumber of triangular numbers to print out
    :return: none
    """
    for number in range(1,n+1):
        print(number,calculate_triangular_number(number), sep="      ")

def calculate_triangular_number(number):
    """
    calculate triangular number
    :param number: number input to calculate, for example 3 => 1 + 2 + 3
    :return: integer
    """
    if number == 1:
        return 1
    else:
        return number + calculate_triangular_number(number-1)
    # sum = 0
    # for number in range(1,n+1):
    #     sum += number
    # return sum
def question2():
    """
    test cases for question 2
    :return:
    """
    testCases = [5,7,3]
    for testCase in testCases:
        print("for testcase:",testCase,"the result is")
        print_triangular_numbers(testCase)
        print("----------")

#---------Question3
def calculate_dots_in_CenteredPentagon(n):
    """
    calculate dots in a centered pentagon shape
    :param n: input index in the list of centered pentagon numbers 1,6,16,31,... for example: n= 2 => return 6
    :return: integer
    """
    # For nth(n>=1) centered pentagon numbers, we have formula: f(n) = (5n^2 - 5n +2)/2
    # I find recursive formula by taking f(n) - f(n-1) = 5n -5 => f(n) = 5(n - 1) + f(n-1)

    # 2nd approach: S(1) = 1 + 0
    # S(2) = S(1) + 5 = 6
    # S(3) = S(2) + 10 = 16
    # S(4) = S(3) + 15 = 31
    # S(n) = S(n-1) + 5(n-1) n starts from 0 to n
    # Base is S(1) = 1


    # Find out that n2 = n1 + 5(n-1) with n = 2
    # n3 = n2 + 5(n-1) with n = 3
    if n == 1:
        return 1
    else:
        return 5*(n-1) + calculate_dots_in_CenteredPentagon(n-1)

def question3():
    """
    test case for question 3
    :return:
    """
    testCases = [5,3,8]
    for testCase in testCases:
        print("for testcase:",testCase,"the result is")
        print(calculate_dots_in_CenteredPentagon(testCase))
        print("----------")



# --------------Homework
def maximumOf(firstNumber,secondNumber):
    """
    Find the maximum between two numbers
    :param firstNumber: first number to compare
    :param secondNumber: second number to compare
    :return: integer
    """
    if firstNumber > secondNumber:
        return firstNumber
    else:
        return secondNumber

def max_collatz(n):
    """
    Return the highest integer in corresponding Collatz sequence
    :param n: input number to find the highest in the Collatz sequence
    :return: integer
    """
    if n ==1:
        return 1
    else:
        if n % 2 == 0:
            return maximumOf(n,max_collatz(n//2))
        else:
            return maximumOf(n,max_collatz(3*n + 1))

def homework():
    """
    test case for homework
    :return:
    """
    testCases = [10,32,85]
    for testCase in testCases:
        print("for testcase:",testCase,"the result is")
        print(max_collatz(testCase))
        print("----------")


main()

# Notes: to do recursive function -> find base and relationship between f(n) and f(n-1)