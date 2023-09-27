##list method
###remove duplicate value 1
##l1=[1,2,3,4,5,6,5,6,3,4]
##print("original value",l1)
##print("remove duplicate value",list(set(l1)))
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
#pattern
#1.
for i in range(2,51,10):
    for j in range(i,i+10,2):
        print(j,end=" ")
    print()
#2.
for i in range(1, 6):
    for j in range(5 - i):
        print(" ",end="")
    for k in range(i):
     print("* ",end="")
    print()
#3.
for i in range(5):
    for i in range(5,0,-1):
        print(i,end="")
    print()
#4.
    count = 1

for i in range(5):  
    for i in range(5):  
        print(count, end=" ")
        count += 1
    print() 
#5.
rows = 5
start_number = 1
number_lists = []

for i in range(rows):
    number_list = [str(start_number + j) for j in range(i + 1)]
    number_lists.append(number_list)
    start_number += i + 1

for row in number_lists:
    print(" ".join(row))
#6.
letter=["A","B","C","D","E"]
for i in range(5):
    print("".join(letter))
#7.
patterns = ["0 1 0 1 0", "1 0 1 0 1"]

for _ in range(3):
    for pattern in patterns:
        print(pattern)
#8.
letter = [
    ['A', 'B', 'C', 'D', 'E'],
    ['F', 'D', 'H', 'I', 'J'],
    ['K', 'L', 'M', 'N', 'O'],
    ['P', 'Q', 'R', 'S', 'T'],
    ['U', 'V', 'W', 'X', 'Y']
]
for i in letter:
    print(' '.join(i))
#9.
for letter in ['A','B','C','D']:
    print(f"{letter*4}")
    
     