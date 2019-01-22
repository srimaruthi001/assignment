# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 09:28:34 2019

@author: srima
"""

#Assignment01

a,b=input("Please enter 2 values ").split(' ')
print(a,b)
print(a+b)
print(a-b)
print(a*b)
try:
    print(a/b)
except ZeroDivisionError:
    print("The divisinon was unsuccesful")

#Assignment 02

a,b,c=input("Please enter 3 values ").split(' ')
a=int(a)
b=int(b)
c=int(c)
big=0
if a > b >  c:
    big=a
elif b > a:
    big =b
elif c > a & c > b:
    big=c
print("The biggest number is %d "%big)

#aSSIGNMENT 03
a = int(input("Please enter a number"))
if a == 0:
    print("Please enter a valid number ")
else:
    if a %2 == 0:
        print("%d is even number "%a)
    else:
        print("%d is an odd number"%a)
        
#Assignment 04
a = int(input("Please enter a number"))
if a == 1 or a == 2 or a == 3:
    print("%d is a prime number"%a)
else:
    for i in range(2,a):
        if a != i:
            if a % i ==0:
                print(i)
                prime=0
                break
            else:
                prime=1
    if prime==1:
        print("%d is a prime number"%a)
    else:
        print("%d is not a prime "%a)

#Assignment 05

a,b,c,d,e=input("Please enter 5 numbers").split(" ")
print(a,'\n',b,'\n',c,'\n',d,'\n',e,'\n')


a,b,c=input("Please enter 3 numbers").split(" ")
a=int(a)
b=int(b)
c=int(c)
big=0
if a > b > c:
    big=a
elif b>c:
    big=b
else:
    big=c
print("the biggest of 3 is %d"%big)

#Assignment 06

str1=input("Enter a string")
if len(str1) > 5:
    print("The substrign is : ",str1[0:5])
    print("The substrign is : ",str1[-5:-2])
else:
    print("Please enter minium 5char length")


print((str1+'\n') * 100)

str2=input("Please enter 2nd string")
print(str1+str2)

#Assignment 07

lst=[1,3,4,5,5,6,7,8,6]
print(type(lst))
for i in lst:
    print(i)

print(lst[1:4])
print(lst[-5:])
print(lst[-4:-1])
print(lst*2)

lst2=['wer','wrwer','wrwr','wrwr34']
print(lst+lst2)

#Assignment 08

tpl=(12,34,34345,234,343,23424,234234,232,1,2,3,4)
print(type(tpl))
for i in tpl:
    print(i)
print(tpl[1:5])
print(tpl[-4:])
print(tpl[-10:-5])
print(tpl*2)

tpl2=('sri','srtt','werw')
print(tpl+tpl2)

#Assignment 09
a=3.14j
b=45.j
print(type(a))
print(a+b)
print(a-b)
print(a*b)
print(a/b)

#Assignment 10
a,b = input("Please enter 2 values ").split(' ')
a=int(a)
b=int(b)

a += b
print(a," ",b)

a -= b
print(a," ",b)
a *= b
print(a," ",b)
a /= b
print(a," ",b)
a **= b
print(a," ",b)
a //= b
print(a," ",b)

#Assignment 11
a,b=input("Enter 2 values ").split(' ')
b=int(b)
a=int(a)

print(a & b)
print(a | b)    
print(a ^ b)
print(~a)
print(a << 2)
print(a >>2)

#Assignment 12
n =1
lst=[]

while n <=10:
    a = input("Please enter a valid number")
    lst.append(int(a))
    n += 1
avg=sum(lst)/len(lst)
s=[]
sm=0
bg=0
b=[]
e=[]
eq=0
for i in lst:
    if i < avg:
        s.append(i)
        sm = sm+1
    elif i > avg:
        b.append(i)
        bg=bg+1
    else:
        e.append(i)
        eq=eq+1
print("%d are less than avg %d "%(sm,avg),s)
print("%d are greater than avg %d "%(bg,avg),b)
print("%d are equal to avg %d "%(eq,avg),e)

#Assignment 13
n=1
a=[]
while n <=4:
    try:
        a.append(int(input("Pllease enter a number")))
        n +=1
    except ValueError:
        print("Enter only numeric values")
b,c,d,e=a
print(b,c,d,e)
if b > c and b > d and b > e:
    big=b
elif c > d and c > e and c > b:
    big = c
elif d > e and d > c and d > b:
    big=d
else:
    big=e
print("The biggest number is %d "%big)
##################################################
n=1
a=[]
while n <=5:
    try:
        a.append(int(input("Pllease enter a number")))
        n +=1
    except ValueError:
        print("Enter only numeric values")
b,c,d,e,f=a
print(b,c,d,e,f)
if b > c and b > d and b > e and b > f:
    big=b
elif c > d and c > e and c > b and c > f:
    big = c
elif d > e and d > c and d > b and d > f:
    big=d
elif e > f and e > d and e > c and e > b:
    big = e
else:
    big=f
print("The biggest number is %d "%big)

#Assignment 14
emp=[2,3,4,5,6,7,8,9,10,11]
name=['sri','ram','par','deep','thul','jag','pus','red','bin','muth']

def print_names(emp,name):
    for i in range(len(emp)):
        print(emp[i]," --> "+name[i])
def read_user_inp(idx,emp,name):
    print(emp[idx]," --> "+name[idx])

def print_4_to_9(emp,name):
    for i in range(4,10):
        print(emp[i]," --> ",name[i])

def print_3_to_end(emp,name):
    for i in range(3,len(emp)):
        print(emp[i]," ---> ",name[i])

def repeat_n_times(no,emp,name):
    print(emp*no,'\n',name*no)

def conc_lists(emp,name):
    print(emp+name)

def print_names_sbs(emp,name):
    for i in range(len(emp)):
        print(emp[i]," --> "+name[i])


print_names(emp,name)
read_user_inp(int(input("Enter an index to display")),emp,name)
print_4_to_9(emp,name)
print_3_to_end(emp,name)
repeat_n_times(int(input("Enter no of times to repeat")),emp,name)
conc_lists(emp,name)
print_names_sbs(emp,name)

#Assignment 15
name=['sri','ram','par','deep','thul']

def check_in(inp,name):
    if inp in name:
        print("The name %s is present in the list "%inp,name)
    else:
        print("There is no such name present inthe list ", name)
        
def check_wo_in(inp,name):
    f = 0
    for i in name:
        if i == inp:
            f=1
            break
        else:
            f=0
    if f ==1:
        print("The name %s is present in the list"%inp,name)
    else:
        print("There is no such name")

def print_Rev(name):
    for i in reversed(name):
        print(i)

check_in(str(input("Enter a name to search")),name)
check_wo_in(str(input("Enter a name to search")),name)
check_wo_in(str(input("Enter a name to search")),name)
print_Rev(name)

#Assignment16

def check_prime(a):
    if a == 1 or a == 2 or a == 3:
        print("%d is a prime number"%a)
    else:
        for i in range(2,a):
            if a != i:
                if a % i ==0:
                    print(i)
                    prime=0
                    break
                else:
                    prime=1
        if prime==1:
            print("%d is a prime number"%a)
        else:
            print("%d is not a prime "%a)

def range_prime(no):
    pr=[]
    for i in range(1,no+1):
        if i > 1:
            for j in range(2,i):
                if i % j == 0:
                    break
            else:
                pr.append(i)
    print(pr)
                
check_prime(int(input("Please enter a number")))
range_prime(int(input("Enter the range")))

#Assignment 17
