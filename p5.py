n= int(input("enter N number: "))

arr=[]
for i in range(n):
    numbers=int(input("enter the number: "))
    arr.append(numbers)
print("maximum is: ",max(arr))
print("minimum is:",min(arr))