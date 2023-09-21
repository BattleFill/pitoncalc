import math
while True:
    print("\nChoose an action")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exponentiation")
    print("6.Square root")
    print("7.Factorial")
    print("8.Sine")
    print("9.Cosine")
    print("10.Tangent")
    print("11.Exit")
    while True:
            try:
                vibor = float(input("What will be your choice?: "))
                break
            except ValueError:
                print("It's not a choice")
    if vibor == 1:       
        while True:
            try:
                chislo1 = float(input("Enter the first number: "))
                break
            except ValueError:
                print("That was no valid number. Try again...")
        while True:
            try:
                chislo2 = float(input("Enter the second number: "))
                break
            except ValueError:
                print("That was no valid number. Try again...")
        result = chislo1 + chislo2
        print(result)
    elif vibor == 2:
        while True:
            try:
                chislo1 = float(input("Enter the first number: "))
                break
            except ValueError:
                print("That was no valid number. Try again...")
        while True:
            try:
                chislo2 = float(input("Enter the second number: "))
                break
            except ValueError:
                print("That was no valid number. Try again...")
        result = chislo1 - chislo2
        print(result)
    elif vibor == 3:
        while True:
            try:
                chislo1 = float(input("Enter the first number: "))
                break
            except ValueError:
                print("That was no valid number. Try again...")
        while True:
            try:
                chislo2 = float(input("Enter the second number: "))
                break
            except ValueError:
                print("That was no valid number. Try again...")
        result = chislo1 * chislo2
        print(result)
    elif vibor == 4:
        while True:
            try:
                chislo1 = float(input("Enter the first number: "))
                break
            except ValueError:
                print("That was no valid number. Try again...")
        while True:
            while True:
                try:
                    chislo2 = float(input("Enter the second number: "))
                    break
                except ValueError:
                    print("That was no valid number. Try again...")
            if chislo2 == 0:
                print("You can't divide by zero")
            else:
                break
        result = chislo1 / chislo2
        print(result)
    elif vibor == 5:
        while True:
            try:
                chislo1 = float(input("Enter the first number: "))
                break
            except ValueError:
                print("That was no valid number. Try again...")
        while True:
            try:
                chislo2 = float(input("Enter the second number: "))
                break
            except ValueError:
                print("That was no valid number. Try again...")
        result = chislo1 ** chislo2
        print(result)
    elif vibor == 6:
        while True:
            try:
                chislo1 = float(input("Enter a number: "))
                break
            except ValueError:
                print("That was no valid number. Try again...")
        result = math.sqrt(chislo1)
        print(result)
    elif vibor == 7:
        while True:
            try:
                chislo1 = float(input("Enter a number: "))
                break
            except ValueError:
                print("That was no valid number. Try again...")
        chislo2 = 1
        while chislo1 > 1:
            chislo2 = chislo2 * chislo1
            chislo1 = chislo1 - 1
        result = chislo2
        print(result)
    elif vibor == 8:
        while True:
            try:
                chislo1 = float(input("Enter a number: "))
                break
            except ValueError:
                print("That was no valid number. Try again...")
        result = math.sin(chislo1)
        print(result)
    elif vibor == 9:
        while True:
            try:
                chislo1 = float(input("Enter a number: "))
                break
            except ValueError:
                print("That was no valid number. Try again...")
        result = math.cos(chislo1)
        print(result)
    elif vibor == 10:
        while True:
            try:
                chislo1 = float(input("Enter a number: "))
                break
            except ValueError:
                print("That was no valid number. Try again...")  
        result = math.tan(chislo1)
        print(result)
    elif vibor == 11:
        break
    else:
        print("\nIt's a bad choise\n ")
    