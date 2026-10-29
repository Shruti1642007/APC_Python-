n=int(input("enter a number:"))
root =int(n ** 0.5)
print("square root of a number is:",root)
count=0
for i in range(1,root+1):
    if root%i==0:
        count+=1
if count==2:
    print("prime number")        
else:
        print("not prime number")    