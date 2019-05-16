#SIMPLE FUNCTIONS

def do_nothing():
    pass

def do_something():
    print("My first function")

def say_hello(name):
    print("Hello", name)

def say_hello_with_age(name, age):
    computer_age = 20

    if computer_age < age:
        print("ekaabo ", name)
    else:
        print("Kaabo ", name)

names = ["ada", "bola", "bisi"]
ages = [18, 20, 25]

# for x,y in zip(names, ages):
#     say_hello_with_age(x,y)

# def sum(num1, num2, num3):
#     print(num1 + num2 +num3)

# sum(5,10, 89)

# def list_summer(_list):
#     sum = 0
#     if isinstance(_list, list):
    
#         for item in _list:
#             sum += item

#         print("the sum of ", _list, "is",sum)
#     else:
#         print(type(_list), "is not a List")


# list_summer([1,2,3,4,5,6])
# list_summer(1)

# do_nothing()
# do_something()
# say_hello("bola")


# products = dict(
#     beans= 100,
#     rice=200,
#     garri= 300,
#     meat= 400,
#     poundo= 150,
#     pork= 250
#  )

# def dict_summer(_dict):
#     sum = 0
#     if isinstance(_dict, dict):
    
#         for key in _dict:
#             sum += _dict[key]

#         print("the sum of ", _dict, "is",sum)
#     else:
#         print(type(_dict), "is not a Dict")

# dict_summer(products)


# def sum(num1 = 0, num2 = 0, num3 = 0):
#     print(num1 , num2 ,num3)

# sum( 5, num3 = 14)

# print(11,2,33, end = "")

# def total(a=5, *numbers, **phonebook):
#     print('a', a)

#     #iterate through all the items in tuple
#     for single_item in numbers:
#         print('single_item', single_item)

#     #iterate through all the items in dictionary    
#     for first_part, second_part in phonebook.items():
#         print(first_part,second_part)

# total([10,9],1,2,3,Jack=1123,John=2231,Inge=1560)











# Simple programme to add two fractions and give answer as fraction 
# def add(a,b):
#         sum = a+b
#         return sum

# def times(a,b):
#         '''This function multiplies two arguments'''
#         multiple = a*b
#         return multiple

# def divide(a,b):
#         divide = a/b
#         return divide

# def frac_man(num1, num2, den1, den2):
#         '''this guy adds two fractions together '''
#         full_den = times(den1,den2)
#         up1 = times(divide(full_den,den1),num1)
#         up2 = (full_den/den2)*num2
#         full_num = up1 + up2
#         return [full_num, full_den]

# def print_man(num1, num2, den1, den2,result):
#         print ("\nAnswer = ", result[0], "/", result[1])
#         print("\n", num1, "/", den1, "+", num2, "/", den2, "is ---> ", result[0], "/", result[1])

# def lower(val):
#         num = val[0]
#         den = val[1]
#         for i in reversed(range(2,10)):
#                 if num % i == 0 and den % i == 0 :
#                         divisible = True
#                         while divisible :
#                                 if num % i == 0 and den % i == 0 :
#                                         num = num/i
#                                         den = den/i
#                                         print(num,den, i)
#                                 else:
#                                         divisible = False
#         return num, den

# num1 = int(input ("Enter Numerator 1 :"))
# den1 = int(input ("Enter Denominator 1 :"))
# num2 = int(input ("Enter Numerator 2 : "))
# den2 = int(input ("Enter Denominator 2 :"))

# result = lower(frac_man(num1, num2, den1, den2))
# print_man(num1, num2, den1, den2,result)


# def greet(_comp, name):
        
#         if name.lower() == 'buhari'.lower():
#                 name = 'Mr President'
#                 greet(_comp, name = name)
                
        
#         resp = '{0} there {1}'.format(_comp,name)

#         return resp

# x = greet(name ='kunle',_comp = 'salute')

# print(x)


# def fg_feeding(amount, period):
#         total_days = period * 30
#         amount_per_day = amount / total_days

#         return (amount_per_day)

# result = fg_feeding(3500000,1)
# print(result, '/day')

# import random

# months = ['jan','feb','mar','apr']
# print(random.randint(0,3))
# word = months[random.randint(0,3)]

# def check(user_input):
        
#         if user_input == word:
#                 print('You were right')
#         else:
#                 print('You were wrong')
    

# user_input = input('Tell me what i picked  jan, mar, apr : ')
# check(user_input)
# x = 60

# def max_val(x,y):

#     print("function x", x)
#     if x > y:
#         return x
#     elif y > x:
#         return y
#     else:
#         return "No greater value"

# print(max_val(23,56))

# print("Global x", x)


# def frac_Man(num1, den1, num2, den2):

#     solved_numerator    = (num1 * den1) + (num2 * den2)
#     solved_denominator  = (den1 * den2) 

#     print("Sum is : ", str(solved_numerator)+"/"+str(solved_denominator) )

# num1 = int(input("Please enter num1 : "))
# den1 = int(input("Please enter den1 : "))
# num2 = int(input("Please enter num2 : "))
# den2 = int(input("Please enter den2 : "))

# frac_Man(num1, den1, num2, den2)


# def frac_Man(num1, den1, num2, den2):

#     solved_numerator    = (num1 * den1) + (num2 * den2)
#     solved_denominator  = (den1 * den2) 

#     num_den = lower([solved_numerator, solved_denominator])#PASSING NUM AND DEN TO THE REDUCING FUNCTION AS A LIST
#     print("Sum is : ", str(num_den[0])+"/"+str(num_den[1]) )

# def lower(val):#PARAMETER HAS TO BE A LIST OF 2 INTEGERS
#         num = val[0]
#         den = val[1]
#         for i in reversed(range(2,10)):
#                 if num % i == 0 and den % i == 0 :
#                         divisible = True
#                         while divisible :
#                                 if num % i == 0 and den % i == 0 :
#                                         num = num/i
#                                         den = den/i
#                                         print(num,den, i)
#                                 else:
#                                         divisible = False
#         return num, den

# num1 = int(input("Please enter num1 : "))
# den1 = int(input("Please enter den1 : "))
# num2 = int(input("Please enter num2 : "))
# den2 = int(input("Please enter den2 : "))

# frac_Man(num1, den1, num2, den2)


# def frac_Man(question):

#         first_break = question.split("+")
#         val1 = first_break[0].split("/")
#         val2 = first_break[1].split("/")

#         num1, den1, num2, den2 = int(val1[0]), int(val1[1]), int(val2[0]), int(val2[1])

#         solved_numerator    = (num1 * den1) + (num2 * den2)
#         solved_denominator  = (den1 * den2) 

#         num_den = lower([solved_numerator, solved_denominator])#PASSING NUM AND DEN TO THE REDUCING FUNCTION AS A LIST
#         print("Sum is : ", str(num_den[0])+"/"+str(num_den[1]) )

def lower(val):#PARAMETER HAS TO BE A LIST OF 2 INTEGERS
        num = val[0]
        den = val[1]
        for i in reversed(range(2,10)):
                if num % i == 0 and den % i == 0 :
                        divisible = True
                        while divisible :
                                if num % i == 0 and den % i == 0 :
                                        num = num/i
                                        den = den/i
                                        print(num,den, i)
                                else:
                                        divisible = False
        return num, den

# question = input("Please enter your question : ")

frac_Man(question)