x=int(input("enter the number: "))
y=int(input("enter the number: "))
print("Before Swapping:\n X=",x,"Y=",y)
temp=x
x=y
y=temp
print("After Swapping:\n X=",x,"Y=",y)

#without temp
a=int(input("enter the number: "))
b=int(input("enter the number: "))
print("Before Swapping:\n a=",a,"b=",b)
a,b=b,a
print("Before Swapping:\n a=",a,"b=",b)

#without using temp,third variable
m=int(input("enter the number: "))
n=int(input("enter the number: "))
print("Before Swapping:\n a=",m,"b=",n)
m=m+n
n=m-n
m=m-n
print("after swapping:\n M=",m,"N= ",n)