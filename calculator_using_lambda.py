opt = int(input("\n\nWhat do you want to do:\n1. Add\n2. Substract\n3. Multiply\n4. Devide\n\nChoose any one option:"))


while opt >= 1 and opt <= 4:
    x = float(input("Enter values: "))
    y = float(input("Enter values: "))

    if opt == 1:
        def addition(a, b): return f"\nResult of {a} + {b} is: {a+b}"
        print(addition(x, y))
        break
    elif opt == 2:
        def substract(a, b): return f"\nResult of {a} - {b} is: {a-b}"
        print(substract(x, y))
        break
    elif opt == 3:
        def multiply(a, b): return f"\nResult of {a} X {b} is: {a*b}"
        print(multiply(x, y))
        break
    elif opt == 4:
        def devide(a, b): return f"\nResult of {a} / {b} is: {a/b}"
        print(devide(x, y))
        break
    else:
        print("Error Occured!!!")
        break
