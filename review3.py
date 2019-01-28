def main():
    # ex1()
    ex2()
    # ex3()



# Given a number n, return True if n is in the range 1..10, inclusive.
# Unless outside_mode is True, in which case return True if the number is less or equal to 1, or greater or equal to 10.
# Print the result returned from your function.

def ex1():
    print("")


def in1to10(n, out):
    numRange = range(1, 11)
    if out:
        return n not in numRange


    else:
        return n in numRange


print(in1to10(5, False))


# Create a function that has a loop that quits with the equal sign.
# If the user doesn't enter the equal sign, ask them to input another string.
# # Once the user enters the equal sign to quit, print all the strings that were entered as one line with each word separated by a comma and space.
def ex2():
    List = []
    userInput = ""
    while (userInput != "="):
        userInput = input("enter a word")
        List.append(userInput)
    print(" ,".join(List))


# Given a non-negative number "num", return True if num is within 2 of a multiple of 10.
# Print the result from your function.
def ex3():
    def nearTen(num):
        myList = [num - 2, num - 1, num + 1, num + 2]

        flag = False
        for eachEl in myList:
            if eachEl % 10 == 0:
                flag = True
                break

        return flag

    print(nearTen(13))
    print(nearTen(18))
    print(nearTen(18))


if __name__ == '__main__':
    main()
