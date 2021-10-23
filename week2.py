def oneB():
    print(9 * 5)

    print(15 / 12)

    print(12 / 15)

    print(15 // 12)

    print(9 % 5)

    print(12 % 15)

    print(6 % 6)

    print(2 + (3 - 1) * 10 / 5 * (2 + 3))

    print(5 ** 2)

    print(5 + (2 + 1) ** 2 ** 3)

    print(16 // 2 * (2 + 2))


def areaOfCircle():
    radius = float(input("input radius "))
    print("area of the circle is " + str((radius ** 2) * 3.14))


def areaOfRect():
    width = float(input("input width "))
    height = float(input("input height "))

    print("area of the circle is " + str(width * height))


def question4():
    startingDay = int(input("input your starting Day "))
    lengthOfStay = int(input("input your length of staying "))

    if startingDay < 0 or startingDay > 7 or lengthOfStay < 0:
        print("starting Day or lengthOfStay input wrong, please try again")
        question4()
    else:
        returnDay = startingDay + lengthOfStay
        while returnDay > 6:
            returnDay -= 7

        print("you will return on Day " + str(returnDay))


def question5():
    P = float(input("input principal Amount: "))
    t = float(input("input number Of Years: "))
    n = 12
    r = 0.08
    print("final Amount A is " + str(P * ((1 + r / n) ** (n * t))))


def challengeExercise():
    maximumStep = 0
    startNumber = 1

    while startNumber < 101:
        step = countStep(startNumber)
        # Question 3
        if step == startNumber:
            print(str(startNumber) + " have the same steps as itself")
        else:
            print(str(startNumber) + " have " + str(step) + " steps")

        # Question 1 & 2
        if maximumStep < step:
            maximumStep = step
            numberWithMaxStep = startNumber

        startNumber += 1

    # Question 1 & 2
    print("number With Most Step is " + str(numberWithMaxStep) + " with " + str(maximumStep) + " steps")


def countStep(number):
    step = 0
    while number != 1:
        if number % 2 == 0:
            number //= 2
            step += 1
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
