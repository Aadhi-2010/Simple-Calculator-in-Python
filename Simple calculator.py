print("Simple Calculator")
a=int(input("Enter the first nnumber:"))
b=int(input("Enter the second nnumber:"))
c=input("Which operation do you wnat to do:\n(a)Multiplication\n(b)Division\n(c)Addition\n(d)Subraction\nChoose the required option:")
if c=="a":
    print("The product is",a*b)
elif c=="b":
    print("The quotient is",a/b)
elif c=="c":
    print("The sum is",a+b)
elif c=="d":
    print("The difference is",a-b)
else:
    print("Invaild input")