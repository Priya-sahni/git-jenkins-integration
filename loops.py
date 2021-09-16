l = int(input("Enter the lower limit :"))
u = int(input("Enter the upper limit :"))
print("Printing only even numbers using While loop")
if (l%2==0):
    print(l)
while (l<=u):
    l=l+1
    if (l%2==0):
        print(l)
print("Printing values using For loop")
x=0
for x in range(l,u):
    print(x)