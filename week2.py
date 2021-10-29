import math


def oneB():
    print("a.", 9 * 5)

    print("b.", 15 / 12)

    print("c.", 12 / 15)

    print("d.", 15 // 12)

    print("e.", 9 % 5)

    print("f.", 12 % 15)

    print("g.", 6 % 6)

    print("h.", 2 + (3 - 1) * 10 / 5 * (2 + 3))

    print("i.", 5 ** 2)

    print("j.", 5 + (2 + 1) ** 2 ** 3)

    print("k.", 16 / 2 * (2 + 2))


def areaOfCircle():
    # ask user to input the radius
    radius = input("input radius ")
    # change data type to float and calculate area
    areaOfCircle = float(radius) ** 2 * 3.14
    # print the area of the circle
    print("area of the circle is", areaOfCircle)


def areaOfRect():
    # ask the user to enter the width and height
    width = float(input("input width: "))
    height = float(input("input height: "))

    # calculate the area of the rectangular
    areaOfRectangle = width * height

    # print out the area of the rectangular
    print("area of the Rectangle is", areaOfRectangle)


def question4():
    # Ask the user to enter the starting Day and the length of stay
    startingDay = int(input("input your starting Day "))
    lengthOfStay = int(input("input your length of staying "))

    # Validate user input to make sure 0 < starting Day < 7 and length Of Stay > 0
    if startingDay < 0 or startingDay > 7 or lengthOfStay < 0:
        print("starting Day or lengthOfStay input wrong, please try again")
        question4()
    else:
        # returnDay will be the sum of starting Day and length of Stay
        returnDay = startingDay + lengthOfStay

        # Handle the case when the returnDay is out of range from 0 to 6
        while returnDay > 6:
            returnDay -= 7

        # Print out the return Day of the user
        print("you will return on Day", returnDay)


def question5():
    # ask the user to input P and t, and initialize n and r
    P = float(input("input principal Amount: "))
    t = float(input("input number Of Years: "))
    n = 12
    r = 0.08
    # calculate the amount A
    A = P * ((1 + r / n) ** (n * t))
    # Print out the result
    print("final Amount A is", A)


def challengeExercise():
    # Initialize the maximum Step to keep track of the maximum step while looping
    maximumStep = 0
    # Initialize the first number to loop over
    startNumber = 1

    # Iterate each number from 1 to 100
    while startNumber < 101:
        # Calculate the step for each number
        step = countStep(startNumber)
        # Question 3: keep track of the number where the step is equal the number itself
        if step == startNumber:
            print(str(startNumber) + " have the same steps as itself")
        # Print out the other numbers with their steps
        else:
            print(str(startNumber) + " have " + str(step) + " steps")

        # Question 1 & 2: keep track of the maximumStep and also the number with that maximum steps
        if maximumStep < step:
            maximumStep = step
            numberWithMaxStep = startNumber

        startNumber += 1

    # Question 1 & 2: Print out the number with the max steps
    print("number With Most Step is " + str(numberWithMaxStep) + " with " + str(maximumStep) + " steps")


def countStep(number):
    # Intialize step variable to store the numbers of steps
    step = 0
    # calulate steps to make the number return to 1 just like the requirements
    while number != 1:
        if number % 2 == 0:
            number //= 2

        else:
            number = 3 * number + 1

        step += 1

    return step


# oneB()
# areaOfCircle()
# areaOfRect()
# question4()
# question5()
challengeExercise()

# Question 4 , 5 still thinking
# Question 5 stop at number = 5 because it make the countStep function into infinite loop
