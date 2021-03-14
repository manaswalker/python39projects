print("""1.Add(+)

         2.Subtract(-)
         
         3.Multiply(*)
         
         4.Divide(/)""")
         
opr=int(input("Choose the option for the operator you want to use"))
a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
if opr==3:
    if a==45:
        if b==3:
            print("555")
elif opr==1:
    if a==56:
        if b==9:
            print("77")
elif opr==4:
    if a==56:
        if b==6:
            print("4")
elif opr==1:
    ans=a+b
    print(ans)
elif opr==2:
    ans=a-b
    print(ans)
elif opr==3:
    ans=a*b
    print(ans)
elif opr==4:
    ans=a/b
    print(ans)
else:
    print("Please Check Your Input!!!!!")
