###|arithmitic opertor|
##a=3
##b=4
##print("addition")
##c=a+b
##print("add:",c)
##print("\n")
##print("subtraction")
##c=a-b
##print("sub:",c)
##print("\n")
##print("multiplication")
##c=a*b
##print("multi:",c)
###|assigment opertor|
##a=4
##b=7
##a+=b
##print("\naddition assigment:",a)#a=11
##a-=b
##print("\nsubtraction assigment:",a)
##a*=b
##print("\nmultiplication assigment:",a)
###|comparsion opertor|
##a=8
##b=10
##print(a==b)
##print(a!=b)
##print(a<b)
##print(a>b)
##print(a<=b)
##print(a>=b)#a=8 b=10 
###|logical opertor|
##a=10
##b=20
##c=30
##d=40
##res=a<b and c<d
##print(res)
##res=a<b or c<d
##print(res)
##res= not a<b# a=10 b=20
##print(res)
##a=2
##b=3
##a,b=b,a
##print(a,b)
##
##print(2<-2)
##print(4>-7)
#|menbership opertor|
##str1="salman"
##str2="salman"
##print(str1 in str2)
##print("\n")
##str1="salman"
##str2="salman"
##print(str1 not in str2)
##print("\n")
###|identity opertor|
##a=34
##b=56
##print(a is b)
##a=34
##b=56
##print(a is not b)
##print(678<-908)
##a=3
##b=7
##a,b=b,a
##print(a,b)
##
##str1 ="ravi"
##str2 ="salman"
##print(str1 is str2)
##print(str1==str2)


a = True
b = False

##print(id(a))
##print(id(b))
##
##print(a is b)
##print(a == b)sa
##
##a=8
##b=6
##print(a is b)
##str1="salman"
##str2="ravi"
##print("ave" in str2)
##
##str1="dev"
##str2="salman"sa
##print("sal" not in str2)
##colan :

##a=3
##b=5
##a,b=b,a
##print(a,b)# swap
#condition opertor
##if(14>6)or(10>89):
##    print("true")
##    print("salman")
##a=8
##if a==10:
##   print("equal")
##elif a==8:
##    print("a is equal")
##else:
##   print("not equal")
#bitwise opertor
#binarya
##print(2&3)
##print(2|3)
##print(2^4)
##print(2<<7)
##print(2>>7)
##print(~2)
##user=input("enter the name:")
##ps=input("enter the password:")
##ouser="salman"
##ops="1234"
##if(user==ouser and ps==ops):
##     print("login is correct")
##else:
##    print("login is incorrect")

#voting
##name=input("enter the name:")
##age=int(input("enter the age:"))
##if(age >= 18):
##    print("eligiable to vote")
##else:
##    print("not eligiable to vote")
#odd or even
##a=int(input("enter the number:"))
##if(a%2==0):
##    print(a,"the number is even")
##else:
##    print(a,"the number is odd")
#vowel
##letter=input("enter the letter:")
##if(letter in ('a','e','i','o','u')):
##    print(letter,"is a vowel")
##else:
##    print(letter,"is a consonat")
#profit or loss
##price=int(input("enter the price:"))
##sellingprice=int(input("enter the selling price:"))
##if(price>selling price):
##    amount=price-sellingprice
##    print("this is loss:",amount)
##elif(sellingprice>price):
##    amount=sellingprice-price
##    print("this is profit:",amount)
##else:
##    print("no profit ,no loss")
#divide by 5
##number=int(input("enter the number:"))
##if(number%5==0):
##    print(number,"hi")
##else:
##    print(number,"bye")
#maximum between two numbers
##a=45
##b=100
##if(a>b):
##    print("the maximum number:",a)
##else:
##    print("the m15aximum number:",b)
##a=10.6
##print(int(a))
##a=10.7
##print(int(10.7))
##print(type(True))
#for loop
#1.sum and average
##sum=0
##count=10
##for i in range(1,11):
##  sum+=i
##print("the sum of 10 numbers",sum)
##average=count*sum
##print("the average of numbers",average)
#2.first 10 natural number
##for i in range(1,11):
##    print(i)
#3.sum of the first 10 natural numbers
##sum=0
##for i in range(1,11):
##   sum=sum+i
##print("the sum of the first 10 natural numbers:",sum)
#4.display n terms of natural numnbers and their sum
##sum=0
##n=int(input("enter the number:"))
##for i in range(1,n+1):
##    sum=sum+i
##print("display n terms of natural numnbers and their sum is:",sum)
#5.cube
##sum=0
##num=int(input("enter the number:"))
##for i in range(1,num+1):
##   sum=sum+pow(i,3)
##print("cube is:",4sum)
#6.multiplication table for a given integer
##sum=0
##num=int(input("enter the number:"))
##for i in range(1,11):
##    sum=sum+i
##print(f"{num}*{i}={num*i}")
#6
##n=int(input("enter the number :"))
##for i in range(1,11):
##   print(n,'*',i,'=',n*i)

##for i in range(1,6):
##    for j in ran5ge(1,6):
##        print(i, end=' ')
##    print()

##for i in range(1,):
##    for j in range(1,11):
##        print(i, end='  ')
##    print()
##
##for i in range(1,6):
##    print(i)
#7.
##num=int(input("enter the number:"))
##for i in range(1,(num+1)):
##    for j in range(1,11):
##        print(i,"*",j,"=",i*j)
#nested loop
##for i in range(1,3):
##     print("week",i)
##     for j in rae4nge(1,3):
##       print("day",j)
##for i in range(1,4):
##  for j in range(1,4):
##   for k in range(1,4):
##     print(i,j,k)
##9.
##for i in range(1,5):
##    print("*"*i)
##10.
##rows=int(input("enter the rows:"))
##for i in range(1, rows+1):
##    for j in range(1, i+1):
##        print(j, end = " ")
##    print()
##11.
##rows=int(input("enter the rows:"))
##for i in range(1, rows+1):
##    for j in range(1, i+1):
##        print(i, end = " ")
##    print()
##12.
##rows=int(input("enter the rows:"))
##number=1
##for i in range(1, rows+1):
##    for j in range(1, i+1):
##        print(number, end = " ")
##        number+=1
##    print()
##13.
##n=int(input("enter the rows:"))
##for i in range(n):
##        for j in range(n-i-1):
##            print("  ",end=" ")
##        for j in range(i+1):
##            print(" * ",end=" ")
##        print()
#1. string slicing
##a="ocean"
##print(a[0])
##--------------------------------------------------------------------------------
##list method
###remove duplicate value 1
##l1=[1,2,3,4,5,6,5,6,3,4]
##print("original value",l1)
##print("remove duplicate value",list(set(l1)))
#sort method 2
##price=[2.22,99.0,80.22]
##price.sort()
##print(price)
#list find the largest number in the list 3
##list=[1,2,3,4,5]
##print("the largest number in the list",(max(list)))
####a=4
####b=5
####a,b=b,a
####print(a,b)
##swap
##list=[23,65,19,90]
##pos1,pos2=2,3
##list[pos1],list[pos2]=list[pos2],list[pos1]
##print(list)
##
##list=[1,2,3,4,5]
##pos1,pos2=2,4
##list[pos1],list[pos2]=list[pos2],list[pos1]
##print(list)
##check if elemnet exist in list in python
##list=[1,2,3,4,5,6]
##i=4
##if i in list:
##    print("elemet is exist")
##else:
##    print("not exist")
##list reverse
##list=[1,2,3,4,5,6,7,8]
##list.reverse()
##print(list)
##lenght without using len
##list=[10,67,78,34,90,6]
##count=0
##for i in list:
##    count+=1
##print("the lenght of the value is",count)
#multiple the number in the list
##list=[4,3]
##multiple=2
##for i in list:
##    multiple*=i
##print(multiple)
#interchange the number
##list=[1,2,3,4,5,6]
##if a:
##    a[0],a[-1]=a[-1],a[0]
##print(a)

##a=[1,2,3,4,5,6]
##x=a[0]
##a[0]=a[a-1]
##print(a)

##a=[1,2,3,4,5]
##if a:
##    a[0],a[-1]=a[-1],a[0]
##print(a)






       
        
    







    




    

    






