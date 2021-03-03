a=(int(input("first"))
b=(int(input("second"))
rem=a%b
while rem!=0:
   a=b
   b=rem
   rem=a%b
   print("GCD is",b)
