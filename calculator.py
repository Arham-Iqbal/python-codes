print("CALCULATOR")
print(" 1.ADDITION ")
print("2.Subtraction ")
print("3.Multiplication ")
print("4.Division ")
print("5.Exit ")
#print("Wrong choice ")
x=int(input("Enter your choice "))
match x:
    case 1: 
        print("ADDITION ")
        print("Enter two numbers  ")
        x=int(input())
        y=int(input())
        print("Sum is ",x+y) 
    case 2:
        print("Subtraction ")
        print("Enter two numbers  ")
        x=int(input())
        y=int(input())
        print("Difference is ",x-y) 
    case 3:
        print("Multiplication ")
        print("Enter two numbers  ")
        x=int(input())
        y=int(input())
        print("Product is ",x*y) 
    case 4:
        print("Division ")
        print("Enter two numbers  ")
        x=int(input())
        y=int(input())
        print("Quotient is ",x/y) 
    case 5:
        print("Exit ")
        exit()
    case _:
        print("Wrong choice ")
    