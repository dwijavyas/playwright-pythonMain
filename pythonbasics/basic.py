a = 3

a, b , c = 1, 2.5, "hello"

print(a)
print(type(c))

print("value of b is ", b)
print(a, "conactenate with", c)
print(a, "conactenate with", b)

#print(a+"concatenate with "+c)

#list - crud
d = ["hey","you", 1, 2.5, 6, "go"]
print(d[4])
print(d[-1]) #last index
print(d[2:5]) #index only 2,3,4
d.insert(3, "bye") #insert
print(d)
d.append("End") #insert at last
print(d)
d[1] = "me" #update
print(d)
del d[0] #delete at index
print(d)
print(type(d))


#tuple - immutable
t = (2,4,5,7)
print(t)
print(type(t))
print(t[2])

#dic
r = {"name":"ram","lastname":"sharma",4:"shyam","code":778, 6:90}
print(r["name"])
print(r[4])
print(r["code"])
print(r["lastname"])
print(r[6])

s = {}

s["key1"] = "value1"
s["key2"] = "value2"
s[3] = "value3"
s[4] = 5
s["key5"] = 6
print(s)

#if else
greeting = "good morning"

if(greeting=="morning"):
    print("condition matches")
else:
    print("condition does not match")
print("if else cond is completed")

a = 10

if a>5:
    print("condition matches")
    print("second line")
else:
    print("condition does not match")
print("if else cond is completed")

#loops
obj = [1,2,5,7,9,10]
for i in obj:
    #print(i)
    #print(i-1)
    print(i*3)

#sum of 1,2,3,4,5
sum = 0
for i in range(1, 6): #i = 1 to i-1 = 5
    sum = sum + i
print(sum)

#first 10 numbers with increment of 2
for k in range(1, 20, 2):
    print(k)

#start from 0
for m in range(10):
    print(m)

#for loop has range, while loop has condition
print("****")
it = 4

while it>1:
    print(it)
    it = it -1 


#when z !=3 print z
print("****")
z = 7

while z>1:
    if(z != 3):
        print(z)
    z=z-1

#when n =3 come out of loop
print("****")
n = 10

while n>1:
    if(n == 3):
        break
    print(n)
    n=n-1

#skip printing 9 and stop at 3  
p=15
while p>1:
    if p == 9:
        p = p - 1
        continue
    if p == 3:
        break
    print(p)
    p = p - 1

#functions
def greetMe(greeting):
    print('hello',greeting)

greetMe("i am heer")

def addIntegers(a,b):
    c=a+b
    print("sum of a and b is",c)

addIntegers(4,5)

def multiply(a,b):
    return a * b

print(multiply(3,4))


#classes
class Calculator:

    def method1():
        print("abc")

    def method2():
        print(12)

Calculator.method1()
Calculator.method2()

#strings
str = "rahulshettyacademy.com"
str2 = "rahul"
print(str[1])
print(str[0:5])

print(str2 in str)

w = str.split(".")
print(w[0])

str4 = " great "
print(str4.strip())

str5 = " hello "
print(str5.lstrip())

str5 = " bye "
print(str5.rstrip())


