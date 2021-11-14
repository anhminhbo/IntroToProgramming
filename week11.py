import math

def main():
    # Problem 1
    # problem_1()

    # Problem 2
    problem_2()

# Problem 1
class Circle:
    def __init__(self,radius):
        self.radius = radius

    def getArea(self):
        return math.pi * self.radius ** 2

    def getPerimeter(self):
        return self.radius * math.pi

def problem_1():
    circy = Circle(11)
    print(circy.getArea())

    circle = Circle(4.44)
    print(circle.getPerimeter())



# Problem 2:
class School:
    __target = 0.99

    def __init__(self, capital):
        self.__budget = capital

    def __max_expenditure(self):
        return self.__budget * School.__target

    def get_target(self):
        return self.__target

    def get_budget(self):
        return self.__budget

    def get_max_expenditure(self):
        return self.__budget * School.__target


def problem_2():
    print(School.get_target(self=School))

    s = School(100000)
    print(s.get_budget())
    print(s.get_max_expenditure())

main()