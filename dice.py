import random
print("This is a dice stimulator")
x = "y"
while x == "y":
    n = random.randrange(1,7)
    if (n == 1):
        print("!-----!\n!     !\n!  0  !\n!     !\n!-----!")
    if (n == 2):
        print("!-----!\n!     !\n! 0 0 !\n!     !\n!-----!")
    if (n == 3):
        print("!-----!\n!  0  !\n!  0  !\n!  0  !\n!-----!")
    if (n == 4):
        print("!-----!\n! 0 0 !\n!     !\n! 0 0 !\n!-----!")
    if (n == 5):
        print("!-----!\n! 0 0 !\n!  0  !\n! 0 0 !\n!-----!")
    if (n == 6):
        print("!-----!\n! 0 0 !\n! 0 0 !\n! 0 0 !\n!-----!")
    x = input("Press y to roll again: ")
