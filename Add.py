"""#1
a=12
b=13
print(a+b)
#2
a=int(input("enter the Value 1 : "))
b=int(input("Enter the value 2 : "))
print(a+b)
#3
a=int(input("Enter Te value : "))
if a==0:
    print("True")
else:
    print("false")
#4
for i in range(1,10):
    print()
    for j in range(1,i+1):
        print(end=("*"))        
#5
a=input("Enter te student name: ")
b=int(input("Enter the number : "))
c=int(input("Enter the Mark Percentage : "))

if c==100:
    print("Very Good")
elif c>=70:
    print("Good")
elif c>=40:
    print("Better")
elif c<40:
    print("Better Luck Next time")
else:
    print("Reappearance")
#6
a=int(input("enter the value : "))
if (a%2==0):
    print("the Number Is Even")
else:
    print("The Number is Odd")
#7
count=0
a=int(input("Enter te Value : "))
for i in range(1,a):
    count=count+1
    print(count)
#8
def value_of_a():
    return 10
a=value_of_a()
print(a)
#9"""
a=10
b=20
def mul_of_ab():
    return a*b
c=mul_of_ab()
print(c)
#10
a=["Orange","banana"]
a.append('Apple')
print(a)