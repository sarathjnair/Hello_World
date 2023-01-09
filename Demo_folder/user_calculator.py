a=input("Enter number 1 : ")
b=input("Enter number 2 : ")
a=int(a)
b=int(b)
if(type(a).__name__=="int" and type(b).__name__ == "int"):
    print(f"The sum of {a} and {b} is {int(a)+int(b)}")
else:
    print("Entered inputs are not integers")