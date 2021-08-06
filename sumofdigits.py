
# creating an empty list
lst = []
 
# number of elements as input
n = int(input())
 
# iterating till the range
for i in range(0, n):
    ele = int(input())
 
    lst.append(str(ele)) # adding the element
     
print(lst)

#process
#print("process of printing")
sum=0
for i in lst:
    sum=0
    for digit in str(i):
       
        sum=int(digit)+sum
    print(sum)
    

