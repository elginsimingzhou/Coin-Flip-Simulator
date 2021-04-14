#Coin Flip Simulation - Write some code that simulates flipping a single coin
#however many times the user decides.
# The code should record the outcomes and count the number of tails and heads.


from random import randint

while True:
    flips = 0
    heads_count = 0
    tails_count = 0

    n = input("How many times do you wish to flip the coin?")

    # string.isnumeric() --> check if it is integer --> returns boolean

    if not n.isnumeric():
        print("Enter a integer")

    else:
        n = int(n)

        if n <= 0:
            print("Please enter a positive integer")

        else:

            while flips < n:

                if randint(0, 1) == 0:
                    heads_count += 1
                else:
                    tails_count += 1
                flips += 1

            print("Number of heads:{}\nNumber of tails:{}".format(heads_count, tails_count))

            choice = input("Do you wish to play again?(Y or N) ")

            if choice[0].upper() == 'N':
                print("Thank you for playing!")
                break

            elif choice[0].upper() == 'Y':
                continue
            else:
                print("Please enter Y or N only!")
                break
