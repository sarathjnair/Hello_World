try:
    a=float(input("Enter number 1 : "))
    b=float(input("Enter number 2 : "))
except Exception:
    print("Please enter a valid input. Entered input is not an integer\n")
else:
    print(f"The sum of {a} and {b} is {a+b}")