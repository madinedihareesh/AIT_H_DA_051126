'''
operators:
10+20
operand1(10) operator(+) operand2(20)
operation:
we can perform an action between two operands is know as operation


diffrent types:
Arithmetic operators (+,-,*,/,%,//,**)
Assignment operators(=,+=,-=,/=,%=)
comparission/relational ship(>,<,>=,<=,==,!=) ## result in boolen expression
logical operators(and,or,not)
bitwise operators (|,^,&,<<,>>)
membership operators(in,not in)
identitiy operators(is,is not)
'''
# a=10
# b=2
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b) ##q divison return the q value in float
# print(a%b) ## r
# print(a//b) ## q floordivison return the q value in int 
# print(a**b)

# print(7/2)
# print(7//2)

# a=10
# a+=10 ## a=a+10 a=10+10 a=20
# print(a) #20
# a-=10 ## a=a-10 a=20-10
# print(a)
# a*=2
# print(a) ##20
# a/=2 ## a=a/2  a=10/2 a=10.0
# print(a) ##10.0
# a%=2 ## a=a%2 reminder a=10.0%2 a=0.0
# print(a)
# a//=2  ##a=a//2 a=0.0 a=0.0//2 0.0
# print(a)
# a**=2
# print(a)

# a=10
# b=2
# print(a>b) ## true
# print(b>a) ## false
# print(b<a) ## true
# print(a<b) ## fale
# print(a>=b) ## a>b a=b
# print(a<=b) ## a,b a=b
# print(a==b) ## flase 10==2
# print(a!=b) ## True

# and or not
# print(True and True) ## True
# print(True and False) ## Flase
# print(False and True) ## Flase 
# print(False and False) ## False

# print(True or False) ## True
# print(True or True) ## True
# print(False or True) ## True
# print(False or False) ## Flase

# print(not True) ## False
# print(not False)## True

# print((10>2) and (2<10))

'''
2 8 10 16
1010 0010

bit binary type
& | ^ << >>
'''
# print(10&2) ## 1010 & 0010

'''
seq
string
list
tuple
'''
# l=[1,2,3,4,5]
# print(1 in l)
# string='Hello World'
# print('W' in string)
# t=(1,2,3,4,5)
# print(6  not in t)

# a=10
# print(id(a))
# b=10
# print(id(b))
# print(a is b) ## id(a) is id(b)

'''
what is the diffrences between == and is
'''

# a=10
# # b=10
# # print(a==b) ## 10 == 10
# # print(a is b) ## id(a) == id(b)
# l=[1,2,3,4,5,6,7,8,9,10]
# print(a==l[9])
# print(a is l[9])

a=None ## Null
b=[10,20,None] ## null

print(a==b) ## none == none
print(a is b[2]) ## id(a) == id(b)