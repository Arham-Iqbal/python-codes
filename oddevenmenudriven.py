print("To check whteher a number is odd or even ")
x=int(input("Enter number "))
match x:
    case x if  x%2==0:
        print("Number is even")
    case x  if x%2!=0:
        print("Number is odd")
    case x if x>0 :
        print("Number is positive ")
    case _:
        print("wrong choice ")

