# i = input("input first value ")
# j = input("input second value ")
#
#
# def printOutRandomValue(i, j):
#     print(i, j)
#
#
# def maxOf(i, j):
#     if i > j:
#         print(i + " is the largest")
#     elif i < j:
#         print(j + " is the largest")
#     else:
#         print("these values are the same")
#
#
# def areaOfRect(i, j):
#     print(int(i) * int(j))
#
#
# def powerOf(i, j):
#     print(int(i) ** int(j))


def checkTriangle():
    # Try ... except to catch error
    try:
        x = int(input("input first side "))
        y = int(input("input second side "))
        z = int(input("input third side "))
        # Check if Triangle is valid
        if x != 0 and y != 0 and z != 0:
            # Check if triangle is right angle or right and isosceles
            if x ** 2 + y ** 2 == z ** 2 or x ** 2 + z ** 2 == y ** 2 or y ** 2 + z ** 2 == x ** 2:
                # Check isosceles
                if x == y or x == z or y == z:
                    print("triangle is isosceles right angle")
                else:
                    print("triangle is right angle")

            #     Check if triangle is equilateral
            elif x == y and x == z:
                print("triangle is equilateral")
            #     Check if Triangle is isosceles
            elif x == y or x == z or y == z:
                print("triangle is isosceles")
            # Last case is a normal triangle
            else:
                print("triangle is scalene")

        else:
            print("this is not a valid triangle, please try again")
            checkTriangle()

    except ValueError:
        print("your input is not a number, please try again")
        checkTriangle()


# printOutRandomValue(i,j)
# maxOf(i,j)
# areaOfRect(i,j)
# powerOf(i,j)

checkTriangle()

