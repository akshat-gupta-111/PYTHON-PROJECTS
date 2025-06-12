try :
    num1 = int(input("Enter first Number: "))
    num2 = int(input("Enter second Number: "))
    print("Choose the operation:\n1. '+' for Addition\n2. '-' for Subtraction\n3. '/' for Divison\n4. '*' for Multiplication\n5. '^' for Power")
    o = input("Input Your Choice: ")

    match o:
        case "+":
            print("sum of both numbers is :",num1 + num2)
        case "-":
            print("difference of both numbers is :",num1 - num2)
        case "/":
            print("first divided by second is :",num1 / num2)
        case "*":
            print("product of both numbers is :",num1 * num2)
        case "^":
            print("first raise to power second is :",num1 ** num2)
        case _:
            print("Not a Valid Operator.")

except Exception as e:
    print(f"Enter the Valid Operations. Error = {e}")