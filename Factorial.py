n=int(input("Enter a number:"))
fact=1
i=n
while i>1:
  fact=fact*i
  i=i-1
print("The factorial of",n,"is",fact)