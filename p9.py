"""
str=input("enter a string: ")
s2=""
for i in str:
    s2=i+s2
if(str==s2):
    print("its palindrome")
else:
    print("not palindrome")

"""

num=int(input("enter a number: "))
temp=num
rev=0
for i in range (len(str(num))):
    digit=num % 10
    rev=rev*10+digit
    num=num//10

if temp==rev:
    print("p")
else:
    print("NP")
