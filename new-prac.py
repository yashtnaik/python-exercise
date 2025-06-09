# # print('Hello, World!')

# # a=int(input('enter the numeric vaue: '))

# # print(f'the entered value is {a}')

# # if (a >= 0):
# #     print("Jai shree Ram")
# # else:
# #     print('Jai shree hanuman')

# # def test_function(a,b):
# #     sum = a + b
# #     print(f'{sum}')

# # test_function(1,2)

# # a=int(input('What is your age?:  '))

# # def odd_even(a):
# #     b = a % 2
# #     if b == 0:
# #         print('Your age is even')
# #     else:
# #         print('your age is odd')

# # odd_even(a)

# numbers=input('Enter the 2 two digits you want to add with space separated: ').split(' ')

# a=int(numbers[0])
# b=int(numbers[1])

# def add(a,b):
#     sum = a + b
#     print(f'the sum of entered numbers is {sum}')

#     if sum % 2 == 0:
#         print(f'The {sum} is a even number hence perform task 1')
#     else:
#         print(f'The {sum} is odd number hence peform task 2')

# add(a,b)


# sum = 0 
# for i in range (1,9): 
#     sum += i
# print (sum)

# print("Hello")
# name=input(str("What is your name?   "))
# print(f'Hello {name} welcome to the project')
# print('what is your age?   ')
# age=input(int())
# print(f'you will be '  +  str(int(age)+1)  +  ' next year')

# rain=input(str('Is it raining outside? Yes or No :'))
# umbrella=input(str('Do you have umbrella? Yes or No :'))

# def isit():
#     still=input(str('Is it still raining?: '))
#     if (still == 'Yes'):
#         print('Wait for a while for rain to stop')
#     else:
#         print('You can go outside')

# if (rain=='Yes' and umbrella=='Yes'):
#     print('You can go outside')
# elif (rain=='Yes' and umbrella=='No'):
#     print('Wait for a while for rain to stop')
#     i=0
#     for i in range (0,6):
#         i +=1
#         print(f'check{i}')
#         isit()
# else:
#     print('You can go outside')

# spam=0

# while spam != 5:
#     print("Hello world")
#     spam += 1

# Name=''
# while Name == '' :
#     print('Enter your name')
#     Name=input()
# print(f'Thank You {Name}')

# for i in range (1,6):
#     print(f'This is {i} Itteration')

# import sys, os, random, pyperclip
# print('Hi Tejas')
# sys.exit()
# print('Hi Tejas')

# import pyperclip
# pyperclip.copy('Tejas is Hasdsome')
# pyperclip.paste()

# def divide42by(num): 
#     try:    
#         value= 42/num
#         print(f'42 divided by {num} is {value}')
#     except ZeroDivisionError:
#         print('ZeroDivisionError: 42 cannot be divided by 0')

# divide42by(2)
# divide42by(3)
# divide42by(0)
# divide42by(4)

# numcats=input('How many cats you have? : ')
# try:
#     if int(numcats) >=4:
#         print('Thats a lot of cats')
#     else:
#         print('That is not many cats')
# except:
#     print('Error: Please enter valid number in digit--- ')

# import random

# secretnum=random.randint(1,10)

# def game():
#     guess=input('Enter your guess between 1 to 10:  ')
#     if secretnum == int(guess):
#         print(f'You guessed the correct answer')
#     elif secretnum != int(guess):
#         print('incorrect answer try again: ')
#     else:
#         break

# for i in range (1,6):
#     game()

# print(f'The correct answer is {secretnum}')

# tejas=['cat','rat','rat','mat',[10,20,30,40,50]]
# el=int(input('enter the element from string between 0-4 :  '))

# if el == 4:
#     sub=int(input('Enter the sublist value between 0-4 :  '))
#     print(tejas[el][sub])
# else:
#     try:
#         print(tejas[el])
#     except:
#         print('invalid input')

# a=[10,20,30,40]
# b=[50,60,70,80]

# def swap_b():
#     for i in range (0,len(a)):
#         b[i]=a[i]
#     print(f'{b}')

# def swap_a():
#     for i in range (0,len(b)):
#         a[i]=b[i]
#     print(f'{a}')

# swap_a()
# swap_b()

# a=[10,20,30,40]
# b=[50,60,70,80]

# def swap():
#     for i in range (0,len(a)):
#         a[i],b[i]=b[i],a[i]
#     print(f'a = {a}  and  b = {b}')
# swap()

# list=['pen','pencil','book','stapler','phone charger']

# for i in range (len(list)):
#     print(f'At inder {i} we have {list[i]}')

# cat = ['Orange', 'Fat', 'loud', 'Grumpy']
# color=cat[0]
# size=cat[1]
# nature=cat[2]
# behaviour=cat[3]
# color, size, nature, behaviour = cat

# tell=str(input('Select what you want to know about your cat : color, size, nature, behaviour :    '))
# ind=cat.index(tell)
# print(f'{ind}')

# cat = ['Orange', 'Fat', 'loud', 'Grumpy']
# numbs=[1,2,4,5,6,3,5,99]
# cat.append(str(input('Enter the string value to append:  ')))
# print(f'{cat}')
# at=int(input('At which location?:  '))
# cat.insert(at, str(input('Enter the string value to insert:  ')))
# print(f'{cat}')
# rm=int(input('Enter the element to remove from the string:  '))

# del cat[rm]
# rrm=str(input('Which element you want to remove?  '))
# print(f'{cat}')
# cat=cat.remove[rrm]
# print(f'{cat}')
# numbs.sort()
# cat.sort()
# print(f'{numbs} and {cat}')

# cat= {'size':'fat', 'name':'mini'}

# print(f'{cat['size']}')
# print(f'{cat.keys()}')
# print(f'{cat.values()}')

# for i in cat.keys():
#     print(f'{i}')

# for i in cat.values():
#     print(f'{i}')

# if 'color' not in cat:
#     cat['color'] = 'orange'
#     print(f'{cat}')

# for i in range (97,123):
# ...         print(chr(i), end=",")
# ...
# Output: c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,

# message="My name is yash and i am the fastest man alive"
# count= {}

# for i in message.upper():
#     count.setdefault(i,0)
#     count[i] = count[i] + 1
# print(count)

# .split()
# .startswith()
# .endswith()
# .center(20,'=')
# .strip()
# .replace('e', 'xyz')

name= 'tejas'
place = 'goa'
dob= '1993'
age= '32'

message= 'my name is %s i live in %s, my year of born is %s, i am %s years old' % (name, place, dob, age)

print(f'{message}')