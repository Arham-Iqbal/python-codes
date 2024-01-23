x=int(input("enter any number: "))
i=2
while i<=x-1:
    if x%i==0:
        break
    i=i+1
if(x==i):
    print("number is prime \n")
else:
    print("not a prime number\n")