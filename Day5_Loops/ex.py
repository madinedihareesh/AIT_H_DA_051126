'''
Loop:
loop is nothing but a repeted block of code until the condition fails

types of loops:
while loop (centinal python)
for loop (for each loop)  (java or javascript (entry contolled loop))



'''

'''

while condtion:
    block of code
'''

# printing 1 - 10 numbers with wile loop

# i=1
# while i<11: ## True/False 11<11
#     print(i)
#     i+=1  ##i=i+1

# print the values from 10-1
# i=10
# while i>=1:
#     print(i)
#     i-=1


# print 1 - 10 only if it is an even number

# i=1
# while i<11:
#     if i%2==0:
#         print(i)
#     i+=1    


'''
for loop


range method (start,stop(excluded),step)
(11) default value of start is 0,default value of step is 1
(1,11) default value step as 1
(1,11,1)
'''

# for i in 'python':
#     print(i)


# for i in [1,2,3,4,5,6]:
#     print(i)


# for i in (1,2,3,4):
#     print(i)


# for i in range(11): 
#     print(i)

# for i in range(1,11):
#     print(i)

# for i in range(1,11,2):  ##loop 1 step 2 1,3
#     print(i)


# for i in range(0,11,2):
#     print(i)

# num=6
# i=1
# count=0
# while i<=num:
#     if num%i==0:
#         print(i)
#         count+=1
#     i+=1
# if count==2:
#     print(num, 'is a prime number')
# else:
#     print(num, 'is not a prime number')        
# else suit
# 
# i=1
# while i<11: # False
#     print(i)
#     i+=1
# else:
#     print('while loop complete')                   

for i in range(1,11):
    print(i)
else:
    print('for loop completed')     