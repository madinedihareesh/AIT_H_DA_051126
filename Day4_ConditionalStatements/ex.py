'''
conditional statements:
simple if
if else
if elif else 
nested condtions
match case

indentation:
either 4 spaces ot one tab space
'''
# simple if 

# a=10
# b=2

# if b>a:
#     print('a is a bigger number')

# age=16

# if age>=18:
#     print('Major')

# input: collect the information in the runtime from the user and by default whater the
# the information we giving it will be in the form of string 


# age=int(input('Enter your age: '))
# if age>=18:
#     print('Major')


# if else
# some conditions will deal with two statements:


# age=int(input('Enter you age: '))
# if age>=18:
#     print('Major')
# else:
#     print('Minor')    


# isticket=False
# if isticket:
#     print('Can watch Movie')
# else:
#     print('can not watch movie')    


# cgpa=int(input('Enter your CGPA: '))
# if cgpa>40:
#     print('Qualified')
# else:
#     print('Not qualified')    

cgpa=int(input('Enter your cgpa'))

if cgpa>=0:
    if cgpa>=90 and cgpa<100:
        print('Grade A')
    elif cgpa>=70 and cgpa<90:
        print('Grade B')
    elif cgpa>=50 and cgpa<70:
        print('Grade C')
    elif cgpa>=36 and cgpa<50:
        print('Grade D')
    else:
        print('Grade F')
else:
    print('Please Enter proper cgpa')        

# mot=input('Enter your MOT: ')
# if mot=='Train':
#     print('I am travlling by train')
# elif mot=='Bus':
#     print('I am travalling by Bus')
# elif mot=='Car':
#     print('I am travalling by Car')
# elif mot=='Flight':
#     print('I am travlling by Flight')
# else:
#     print('I am not travlling')                
