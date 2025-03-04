lower=int(input("Enter the lower range number:"))
upper=int(input("Enter the upper range number:"))
print("Prime numbers between lower and upper range are:")
for num in range(lower,upper+1):
 if num >1:
   for i in range(2,num):
    if num%i==0:
      break
   else:
    print(num)