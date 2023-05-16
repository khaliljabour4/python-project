import math

def scientific_calculator():
    print("Scientific Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square root")
    print("6. Logarithm")
    print("7. Sine")
    print("8. Cosine")
    print("9. Tangent")
    print("10. Quit")
    
    choice = int(input("Enter choice (1-10): "))

    if choice == 1:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1, "+", num2, "=", num1 + num2)

    elif choice == 2:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1, "-", num2, "=", num1 - num2)

    elif choice == 3:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1, "*", num2, "=", num1 * num2)

    elif choice == 4:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            print(num1, "/", num2, "=", num1 / num2)

    elif choice == 5:
        num = float(input("Enter a number: "))
        print("Square root of", num, "is", math.sqrt(num))

    elif choice == 6:
        num = float(input("Enter a number: "))
        print("Logarithm base 10 of", num, "is", math.log10(num))

    elif choice == 7:
        num = float(input("Enter a number in degrees: "))
        print("Sine of", num, "degrees is", math.sin(math.radians(num)))

    elif choice == 8:
        num = float(input("Enter a number in degrees: "))
        print("Cosine of", num, "degrees is", math.cos(math.radians(num)))

    elif choice == 9:
        num = float(input("Enter a number in degrees: "))
        print("Tangent of", num, "degrees is", math.tan(math.radians(num)))

    elif choice == 10:
        print("Exiting the calculator...")
        exit()

    else:
        print("Invalid choice")
        
while True:
    scientific_calculator()
