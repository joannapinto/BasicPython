str1=input("Enter a word:")
str2=str1[::-1]
print("The reversed string is",str2)
if str1==str2:
  print("It is a palindrome")
else:
  print("It is not a palindrome")