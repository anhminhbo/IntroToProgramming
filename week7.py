import random

def main():
    """
    Week 7 function running here
    :return: none
    """

    #Question 2:
    # multiplication_table(100)

    #Question 3:
    # print_numbers_of_digits(1000)

    #Question 4:
    # print_reverse_string("minhporo")

    #Question 5:
    # print(isPalindrome("Able was I ere I saw Elba"))

    #Question 6:
    # print(removeSpecificLetterFromString("a", "abc abcbascbasb aaaaawww"))

    #Question 7:
    # print(removeSpecificSubStringFromString("abc","abcef fegabcasd asdasdasabc"))

    #Question 8:
    randomList = getRandomAlphebeticalCharactersOrders()
    encryptedString = encrytionOf("MINHPORO",randomList)
    print(encryptedString)
    #Question 9
    print(decryptionOf(encryptedString,randomList))

# Question 1: a) y
# b) g
# c) 9
# d) Myst
# e) true
# f) true
# g) true
# h) false
# i) False

#--------------------Question 2
def multiplication_table(n):
    """
    create a multiplication table size nxn®
    :param n: input integer to create a multiplication table size nxn
    :return: none
    """
    x = "x"

    # Calculate the length of maximum number in the table
    lengthOfLargestMultiplication = len(str(n**2))

    # 1st row and 1st column is used to format the table -> range(n+1)
    # multiplication of 0 also -> range(n+1+1) = range(n+2)
    for row in range(n+2):
        for column in range(n+2):
            # "int:int" to format the display integer to minimum of length of the int
            # Handle first row case to format the table
            if row == 0:
                # Handle the first element at (0,0) --> "x"
                if column == 0:
                    # format string:>int to display with the minimum length of the int
                    print(f"{x:>{lengthOfLargestMultiplication}}" ,end=" ")
                else:
                    print(f"{column-1:{lengthOfLargestMultiplication}}", end=" ")

            else:
                # Handle the first column in the table to format
                if column == 0:
                    print(f"{row - 1:{lengthOfLargestMultiplication}}", end=" ")
                else:
                    print(f"{(row-1) * (column-1):{lengthOfLargestMultiplication}}",end= " ")
        # Create a new line between each row
        print()

    # for row in range(n + 1):
    #     print(*(f"{(row * col):{len(str(n*n))}}" for col in range(n + 1)))


#-------------------Question3:
def digitsOf(n):
    """
    Return numbers of digits in an integer
    :param n: input integer
    :return: integer
    """
    return len(str(n))

def print_numbers_of_digits(n):
    """
    Print numbers of digits
    :param n: input integer
    :return: none
    """
    print("Numbers of digits of",n,"is",digitsOf(n))

#-------------------Question4:
def reverseString(inputString):
    """
    return reverse string
    :param inputString: input String
    :return: string
    """
    return inputString[::-1]

def print_reverse_string(inputString):
    """
    print reverse string
    :param inputString: input String
    :return: none
    """
    print("reverse string of",inputString,"is",reverseString(inputString))

#-------------------Question5:
def isPalindrome(inputString):
    """
    Check if the input string is palindrome or not
    :param inputString: input string
    :return: boolean
    """
    formattedInputString = formatString(inputString)
    print(formattedInputString)
    if reverseString(formattedInputString) == formattedInputString:
        return True
    else:
        return False


def formatString(inputString):
    """
    format String before put to check Palindrome
    :param inputString: input string
    :return: string
    """

    return removeAllSpaceInString(inputString).upper()

#-------------------Question6:
def removeSpecificLetterFromString(removeChar,inputString):
    """
    Remove specific letters from string
    :param inputString: input string
    :param removeChar: character need to be removed
    :return: string
    """

    # result = ""
    # for char in inputString:
    #     if removeChar == char:
    #         continue
    #     else:
    #         result += char
    #
    # return  result

    if removeChar in inputString:
        return inputString.replace(removeChar,"",-1)

#-------------------Question7:
def removeSpecificSubStringFromString(removeSubString,inputString):
    """
    Remove specific substring from string
    :param inputString: input string
    :param removeSubString: subString need to be removed
    :return: string
    """
    if removeSubString in inputString:
        return  inputString.replace(removeSubString,"",-1)


#-------------------Question8:
def getRandomAlphebeticalCharactersOrders():
    """
    return random alphebetical Characters Orders Lists
    :return: list
    """

    listOf26Characters = list("QTGABCDEFHIJKLMNOPRSUVXYZW")
    random.shuffle(listOf26Characters)

    print("your random mapping of characters to encrypt and decrypt is", "".join(listOf26Characters))
    return listOf26Characters


def encrytionOf(inputString,randomList):
    """
    encrypt input string
    :param inputString: input string
    :param randomList: random alphabetical list
    :return: string
    """

    orderedList = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


    formattedString = formatString(inputString)

    result = ""

    # Handle case randomList the same as orderedList
    while randomList == orderedList:
        randomList = getRandomAlphebeticalCharactersOrders()

    # for each character in input string, replace with a new character in the randomList
    for char in formattedString:
        result += char.replace(char,randomList[orderedList.index(char)],1)



    return result

def decryptionOf(encryptedString,randomList):
    """
    Decrypte the encrypted string to its original
    :param encryptedString:
    :param randomList:
    :return: string
    """
    orderedList = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    result = ""

    for char in encryptedString:
        result += char.replace(char,orderedList[randomList.index(char)],1)

    return result

def removeAllSpaceInString(inputString):
    """
    remove all space in string
    :param inputString: input string
    :return: string
    """
    return ''.join(inputString.split())

main()