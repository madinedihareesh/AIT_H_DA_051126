'''
We have utilized a loop inside another nested loops
'''
# i=1
# while i<101:
#     count=0
#     j=1
#     while j<=i:
#         if i%j==0:
#             count+=1
#         j+=1
#     if count==2:
#         print(i, 'is a prime number')
#     i+=1            


# 1234
# each and every digit of a number
# % reminder 1234%10 =10)1234-1230(123 =4 num//=10

# num=1234
# while num>0:
#     res=num%10
#     print(res)
#     num//=10

# add all the digit in a number

# num=int(input('Enter the value: '))
# count=0
# while num>0:
#     res=num%10
#     count+=res
#     num//=10
# else:
#     print('sum of the digits in the number',count)


# num=1221
# clone=num ## copy of a number
# rev=0
# while num>0:
#     res=num%10
#     rev=rev*10+res
#     num//=10
# if clone==rev:
#     print(clone,'is a palndrome of a number')
# else:
#     print(clone,'is not a palndrome')  

# i=1
# a=0
# b=1
# while i<11:
#     print(a)
#     c=a+b
#     a=b
#     b=c
#     i+=1

'''
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *

*
* *
* * *
* * * * 
* * * * *
'''

# i=1
# while i<6:
#     j=1
#     while j<6:
#         print('*',end=' ')
#         j+=1
#     print()
#     i+=1    

i=1
while i<6:
    j=1
    while j<6:
        if i>=j:
            print('*',end=' ')
        j+=1
    print()
    i+=1 



