
i=1
while i<=3:
    print("Enter an even number")
    x=int(input())
    if x%2==0:
       print("YOU WON")
       break
    i+=1
else:
    print("YOU LOOSE")