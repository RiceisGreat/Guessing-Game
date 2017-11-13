import random

choice = ''
dec = ''
dif = ''
counter = 0
g1 = ''
g2 = ''


def imp2():
    global dif, dec, counter, g1, g2

    x = random.randrange(1, 11)
    y = 0
    g1 = counter
    g2 = counter
    counter = 0

    print(" \n INSTRUCTIONS: P1 starts first, after P1 guesses the number, P2 goes."
          " \n After P1 and P2 go, the round is over."
          " \n Person with least amount of guesses after the round is the winner.")

    print(" \n P1's turn")

    while y != x:
        g1 += 1

        y = int(input(" \n ENTER a number BETWEEN 1 & 10000:"))

        if y > x:
            print(" \n LOWER")

        elif y < x:
            print(" \n HIGHER")

        else:
            print(" \n You guessed the RIGHT number.")

            print(" \n P2's turn")

    x = random.randrange(1, 11)

    while y != x:
        g2 += 1

        y = int(input(" \n ENTER a number BETWEEN 1 & 10000:"))

        if y > x:
            print(" \n LOWER")

        elif y < x:
            print(" \n HIGHER")

        else:
            print(" \n You guessed the RIGHT number.")

            print(" \n End Round")

            print(" P1 Number of guesses:" + str(g1))
            print(" P2 Number of guesses:" + str(g2))


def hard2():
    global dif, dec, counter, g1, g2

    x = random.randrange(1, 11)
    y = 0
    g1 = counter
    g2 = counter
    counter = 0

    print(" \n INSTRUCTIONS: P1 starts first, after P1 guesses the number, P2 goes."
          " \n After P1 and P2 go, the round is over."
          " \n Person with least amount of guesses after the round is the winner.")

    print(" \n P1's turn")

    while y != x:
        g1 += 1

        y = int(input(" \n ENTER a number BETWEEN 1 & 100:"))

        if y > x:
            print(" \n LOWER")

        elif y < x:
            print(" \n HIGHER")

        else:
            print(" \n You guessed the RIGHT number.")

            print(" \n P2's turn")

    x = random.randrange(1, 11)

    while y != x:
        g2 += 1

        y = int(input(" \n ENTER a number BETWEEN 1 & 100:"))

        if y > x:
            print(" \n LOWER")

        elif y < x:
            print(" \n HIGHER")

        else:
            print(" \n You guessed the RIGHT number.")

            print(" \n End Round")

            print(" P1 Number of guesses:" + str(g1))
            print(" P2 Number of guesses:" + str(g2))


def inte2():
    global dif, dec, counter, g1, g2

    x = random.randrange(1, 11)
    y = 0
    g1 = counter
    g2 = counter
    counter = 0

    print(" \n INSTRUCTIONS: P1 starts first, after P1 guesses the number, P2 goes."
          " \n After P1 and P2 go, the round is over."
          " \n Person with least amount of guesses after the round is the winner.")

    print(" \n P1's turn")

    while y != x:
        g1 += 1

        y = int(input(" \n ENTER a number BETWEEN 1 & 20:"))

        if y > x:
            print(" \n LOWER")

        elif y < x:
            print(" \n HIGHER")

        else:
            print(" \n You guessed the RIGHT number.")

            print(" \n P2's turn")

    x = random.randrange(1, 11)

    while y != x:
        g2 += 1

        y = int(input(" \n ENTER a number BETWEEN 1 & 20:"))

        if y > x:
            print(" \n LOWER")

        elif y < x:
            print(" \n HIGHER")

        else:
            print(" \n You guessed the RIGHT number.")

            print(" \n End Round")

            print(" P1 Number of guesses:" + str(g1))
            print(" P2 Number of guesses:" + str(g2))


def meh2():
    global dif, dec, counter, g1, g2

    x = random.randrange(1, 11)
    y = 0
    g1 = counter
    g2 = counter
    counter = 0

    print(" \n INSTRUCTIONS: P1 starts first, after P1 guesses the number, P2 goes."
          " \n After P1 and P2 go, the round is over."
          " \n Person with least amount of guesses after the round is the winner.")

    print(" \n P1's turn")

    while y != x:
        g1 += 1

        y = int(input(" \n ENTER a number BETWEEN 1 & 10:"))

        if y > x:
            print(" \n LOWER")

        elif y < x:
            print(" \n HIGHER")

        else:
            print(" \n You guessed the RIGHT number.")

            print(" \n P2's turn")

    x = random.randrange(1, 11)

    while y != x:
        g2 += 1

        y = int(input(" \n ENTER a number BETWEEN 1 & 10:"))

        if y > x:
            print(" \n LOWER")

        elif y < x:
            print(" \n HIGHER")

        else:
            print(" \n You guessed the RIGHT number.")

            print(" \n End Round")

            print(" P1 Number of guesses:" + str(g1))
            print(" P2 Number of guesses:" + str(g2))


def imp():
    global dec, dif, counter

    x = random.randrange(1, 10001)
    y = 0
    counter = 0

    while y != x:
        counter += 1
        y = int(input(" \n ENTER a number BETWEEN 1 & 10001:"))

        if y > x:
            print(" \n LOWER")
        elif y < x:
            print(" \n HIGHER")
        else:
            print(" \n You guessed the RIGHT number.")
            print(" Number of guesses:" + str(counter))

            print(" \n Play Again?")

            print(" \n 1. YES \n 2. NO")

            dec = int(raw_input("\n Type the number, 1 = YES, 2 = NO:"))

            if dec == 1:
                print(" \n Would You like to change the difficulty?")
                print(" \n 1. YES \n 2. NO")

                dif = int(raw_input("\n Type the number, 1 = YES, 2 = NO:"))
                if dif == 1:
                    main()
                else:
                    imp()
            else:
                print(" \n Thanks for PLAYING!")


def hard():
    global dec, dif, counter

    x = random.randrange(1, 101)
    y = 0
    counter = 0

    while y != x:
        counter += 1
        y = int(input(" \n ENTER a number BETWEEN 1 & 101:"))

        if y > x:
            print(" \n LOWER")
        elif y < x:
            print(" \n HIGHER")
        else:
            print(" \n You guessed the RIGHT number.")
            print(" Number of guesses:" + str(counter))

            print(" \n Play Again?")

            print(" \n 1. YES \n 2. NO")

            dec = int(raw_input("\n Type the number, 1 = YES, 2 = NO:"))

            if dec == 1:
                print(" \n Would You like to change the difficulty?")
                print(" \n 1. YES \n 2. NO")

                dif = int(raw_input("\n Type the number, 1 = YES, 2 = NO:"))
                if dif == 1:
                    main()
                else:
                    hard()
            else:
                print(" \n Thanks for PLAYING!")


def inte():
    global dec, dif, counter

    x = random.randrange(1, 21)
    y = 0
    counter = 0

    while y != x:
        counter += 1
        y = int(input(" \n ENTER a number BETWEEN 1 & 20:"))

        if y > x:
            print(" \n LOWER")
        elif y < x:
            print(" \n HIGHER")
        else:
            print(" \n You guessed the RIGHT number.")
            print(" Number of guesses:" + str(counter))

            print(" \n Play Again?")

            print(" \n 1. YES \n 2. NO")

            dec = int(raw_input("\n Type the number, 1 = YES, 2 = NO:"))

            if dec == 1:
                print(" \n Would You like to change the difficulty?")
                print(" \n 1. YES \n 2. NO")

                dif = int(raw_input("\n Type the number, 1 = YES, 2 = NO:"))
                if dif == 1:
                    main()
                else:
                    inte()
            else:
                print(" \n Thanks for PLAYING!")


def meh():
    global dif, dec, counter

    x = random.randrange(1, 11)
    y = 0
    counter = 0

    while y != x:
        counter += 1
        y = int(input(" \n ENTER a number BETWEEN 1 & 10:"))

        if y > x:
            print(" \n LOWER")

        elif y < x:
            print(" \n HIGHER")

        else:
            print(" \n You guessed the RIGHT number.")
            print(" Number of guesses:" + str(counter))

            print(" \n Play Again?")

            print(" \n 1. YES \n 2. NO")

            dec = int(raw_input("\n Type the number, 1 = YES, 2 = NO:"))

            if dec == 1:
                print(" \n Would You like to change the difficulty?")
                print(" \n 1. YES \n 2. NO")

                dif = int(raw_input("\n Type the number, 1 = YES, 2 = NO:"))
                if dif == 1:
                    main()
                else:
                    meh()
            else:
                print(" \n Thanks for PLAYING!")


def main():
    global choice

    print(" \n HELLO there, this is a GAME, a SIMPLE guessing game.  I hope you ENJOY.")

    print(" \n Choose a mode")

    print(" \n 1. Singleplayer \n 2. Multiplayer ")

    choice = int(raw_input("\n Type the number that corresponds with the difficulty:"))

    if choice == 1:
        print(" \n Choose a difficulty:")

        print(" \n 1. Meh \n 2. Intermediate \n 3. Hard \n 4. Impossible")

        choice = int(raw_input("\n Type the number that corresponds with the difficulty:"))

        if choice == 1:
            meh()
        elif choice == 2:
            inte()
        elif choice == 3:
            hard()
        else:
            imp()
    else:
        print(" \n Choose a difficulty:")

        print(" \n 1. Meh \n 2. Intermediate \n 3. Hard \n 4. Impossible")

        choice = int(raw_input("\n Type the number that corresponds with the difficulty:"))

        if choice == 1:
            meh2()
        elif choice == 2:
            inte2()
        elif choice == 3:
            hard2()
        else:
            imp2()


main()