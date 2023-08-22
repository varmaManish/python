print("Hello World!")
x=input("Enter First No.:")
y=input("Enter Second No.:")
z=int(x)+int(y)
print("The addition is:",z)
n=int(x)-int(y)
print("The subtarction is:",n)
k=int(x)*int(y)
print("The multiplication is:",k)
s=int(x)/int(y)
print("The division is:",s)
r=int(input("Enter a No.:"))
if(r%2)==0:
  print("{0} is Even number".format(r))
else:
  print("{0} is Odd number".format(r))
p=int(input("Enter a number:"))
Fact=1
For i in range(1,p+1):
Fact=Fact*i
print("The Factorial of",p,"is",Fact)
