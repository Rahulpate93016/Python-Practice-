import random
n=random.randint(1,10)
a=-1
guess=0
while(a !=n):
  guess+=1
  a=int(input("Geuss the number"))
  if(a>n):
   print("lower number please")
  else:
    print("Higher number please")
print(f"You Guess write number is {n} correctly guess is   {guess} attempts")