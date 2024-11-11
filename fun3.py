# Find the maximum number of given number
def max(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and  b>c):
       return b
    else:
        if(c>a and c>b):
            return c
        

a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
c=int(input("Enter the Third number"))
print(f"The max number is {max(a,b,c)}")