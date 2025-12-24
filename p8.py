str=input("enter a string: ")
str=str.casefold()
if str==str[::-1]:
    print("its palindrome")
else:
    print("not a palindrome")