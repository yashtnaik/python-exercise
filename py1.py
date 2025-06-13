# age = int(input("Hi what is your age?   "))
# name = input("what is your name?    ")
# print(f"{name} is {age} years old")

# if age >= 18:
#     print("He is an adult!")
# else:
#     print("He is a minor")

# x = 0
# a = 6
# b = 6
# if a > 0:
#     if b < 0: 
#         x = x + 6 
#     elif a > 6:
#         x = x + 5
#     else:
#         x = x + 4
# else:
#     x = x + 3

# print(x)

# Guess = int(input("Guess a number :  "))
# secret_number = 5
# while Guess != secret_number:
#     Guess = int(input("Guess a number :  "))
# if Guess == secret_number:
#         print(f'Your Guess is correct, the secret number is {Guess}')

# i = 5
# while True:
#     if i%11 == 0:
#         break
#     print(i)
#     i += 2

# a = int(input("Mr.A input your age:   "))
# b = int(input("Mr.B inpt your age:   "))

# if (a and b >= 18):
#     print("A and B are both adults")
# elif (a >= 18 and b < 18):
#     print("A is an adult and B is minor")
# elif (b >= 18 and a < 18):
#     print("B is an adult and A is minor")
# elif (a < 18 and b < 18):
#     print("Both A and B are minors")
# else:
#     print("provide valid inputs")


# hungry = input("Are you hungry?  Provide True or False:       ")
# a = hungry.lower()

# if (a == "true"):
#     print("you are hungry")
# elif (a == "false"):
#     print("you are not hungry")


# names = ["Tejas", "Naik", "Gauri", "shetty"]

# print(names[3])
# del names[2]
# names[1] = "yash"
# print(len(names))

# ages = [25,53,44,22,13]
# total = 0
# people = len(ages)
# for i in ages:
#     total += i
#     i + 1
# avg = (total / people)
# print(f"{avg}")

# def input_number():
#     return int(input("enter 2 numbers:  "))

# a = input_number()
# b = input_number()

# name = input("what is your name?:  ")

# print(f'{name} enter {a} as first number and {b} as second' )

# def sum_calculator(num1,num2):
#     sum = num1 + num2
#     if (sum == 0):
#         return
#     print(f'sum of the entered values is : {sum}')

# sum_calculator(10,-20)

# def odd_even(num):
#     a = num % 2
#     if ( a == 0):
#         return True
#     else:
#         return False

# print(odd_even(22))

# def multiply_values(list):
#     multiplied_values = []
#     for i in list:
#         multiplied_values.append(i * 2)
#     print(multiplied_values)
#     return multiplied_values

# multiply_values([1,2,3,4,5])

# a = [1,2,3,4,5]
# def replace_item(list):
#     list[2] = 9
# replace_item(a)
# print(a)

# .upper()
# .lower()
# .split(',')
# .replace('a', 'xyz')
# .isdecimal()   ---numbers only
# .isalpha()   ---letters only
# .isalnum()   ---letters and numbers only
# .isspace()   ---whitespace only
# .ittitle()   ---title case only ( Example Of Title Case Where First Character Is Capital)
# .isupper()   ---to check if upper case
# .islower()   --- to check if lower case
# .startswith()   ---to check
# .endswith()   ---to check
# .center(20,"=")  ---center align by 10 characts both side
# .rjust(10)  ---right adjust by 10
# .ljust(10)  ---left adjust by 10
# .strip()   --- removed the whitespaces
# .rstrip()  --- removes the whitespaces on right
# .lstrip()  --- removes the whitespaces on left

# name='tejas'
# age='32'
# place='goa'
# dob='1993'

# message='My name is %s, I am %s years old, My native place is %s, my born year is %s' % (name,age,place,dob)
# print(f'{message}')


# import os, shutil

# os.chdir('c:\\USERS\\yenaik\\Desktop')

# for filename in os.listdir():
#     if filename.endswith('.txt'):
#         print(filename)
#         os.remove(filename)

# 20250404

# import os

# os.chdir('c:\\path')
# for logs in os.listdir():
#     if logs.startswith('20250404'):
#         os.remove(logs)

# a=[1, 2, 3, 4, 5, 6]
# b=[7, 8, 9, 10, 11]
# try:
#     for i in range (len(a)):
#         a[i],b[i] = b[i],a[i]
#     print(f'New a set is {a} and \nNew b set is {b}')
# except:
#     print('Some error occured')

'''
*****
*   *
*   *
*   *
*****
'''
# def box(symbol, width, height):
#     if len(symbol) != 1:
#         raise Exception('Symbol should be a single character')
#     if (width) >= 15:
#         raise Exception('width should be less tha 15')
#     print(symbol * width)
#     for i in range(height -2):
#         print(symbol + (' '* (width-2)) + symbol )
#     print(symbol * width)
# box('*', 16, 5)

# import os, re, shutil
# try:
#     os.chdir('c:\\Users\\yn1010\\Desktop\\ITDefined Data\\python\\python-exercise')
#     logfile=open(r'c:\\Users\\yn1010\\Desktop\\ITDefined Data\\python\\python-exercise\\log.txt')
#     data=logfile.read()
#     ipregx=re.compile(r'\b(?:\d{1,3}\.)(?:\d{1,3}\.)(?:\d{1,3}\.)(?:\d{1,3})\b')
#     ipout=ipregx.findall(data)

#     print(ipout)
# except:
#     print('Invalid data type, file not found')

# name=input('what is your name?: ')
# age=int(input('What is you age?: '))

# if name.lower() == 'alice' and age >=18 :
#     print(f'Hi {name}, nice to meet you')
# elif name.lower() == 'alice' and age <18 :
#     print('You are not the Alice we want, Kiddo')
# else:
#     print(f'Ending the conversation with {name}')

# spam = 0

# while spam < 5 :
#     print('Hi Tejas')
#     spam += 1

# name=''

# while name.lower() != 'tejas':
#     print('Type your name here: ')
#     name=input()
# else:
#     print(f'Nice to meet you {name}')

# spam = 0

# while spam < 5:
#     # print(f'spam value is {spam}')
#     spam += 1
#     if spam == 3:
#         continue
#     print(f'spam value is {spam}')

# for i in range (0,5):
#     print(f'My name is Yash for {i}')

# import math, sys 

# nut=int(input("Enter the value to divide 42:  "))

# def divide42by(nut):
#     try:
# ``      ans = 42/num
#         print(ans)
#     except:
#         print("error")
# divide42by()

# cats=int(input('Enter the number of cats you have:  '))

# try: 
#     if cats >= 4:
#         print('Thats a lot of cats')
#     else:
#         print('That is not that many cats')
# except ValueError:
#     print('Invalid input error')

# import random

# ans=random.randint(0,10)
# guess=int(input('Guess the number between 1 to 10:   '))

# for attempt in range(0,6):
#     if guess == ans:
#         print('Guessed correctly')
#     else:
#         print('Try again')

# supplies=['tea', 'butter', 'milk', 'bread']

# for i in range(len(supplies)):
#     print(f'at {i} we have {supplies[i]}')


