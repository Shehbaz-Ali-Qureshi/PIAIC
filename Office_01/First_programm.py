print("my name is ali.", "my age is 21.")
name = "ali"  #string
age = 21      #inte
price = 25.99 #float
print(name)
print(age)
print(price)
#print type
name = "ali"  
age = 21      
price = 25.99 
print(type(name))
print(type(age))
print(type(price))
#print sum
a = 5
b = 6 
sum = (a + b) 
print(sum)
#expression execution/repeat
A, B= 2, 3
Txt = "@"
print(2*Txt*3)
#Concatenation
A, B= "2", 3
Txt = "@"
print((A+Txt)*B)
#Arithmetic operators
A,B= 2,3
c=4
print(a+b*c)
#Arithmetic expression int & float
a = 10 
b = 5.0
c = a*B
print(c)
#Integer division / /
a = 12
b = 5
c = a // b
print(c)
#Input in python
#String input
name = input("name : ")
print(name)
#integer input
age = int(input("age : "))
print(age)
#float input
price = float(input("price : "))
print(price)
#Condition statements
# if_elif_else(SYNTAX)
light = input("light colour : ")
if(light == "red"):
    print("stop")
elif(light == "yellow"):
    print("look")
elif(light == "green"):
    print("go")
else:
    print("light is broken")