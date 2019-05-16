# RETURN STATEMENT
# def stupid_func(): #NO INPUT NO OUTPUT
#     print("i am a stupid function")

# print(stupid_func())

# def stupid_func2(input1): # ONE INPUT NO OUTPUT
#     print(f"i am a stupid function one input {input1}")

# print(stupid_func2(1))

# def stupid_func3(input1, input2): # TWO INPUT NO OUTPUT
#     print(f"i am a stupid function one input {input1}, {input2}")


# print(stupid_func3(1,2))

# def smart(input1, input2): # TWO INPUT WITH OUTPUT
#     print(f"i am a stupid function one input {input1}, {input2}")

#     return 23

# print(smart(1,2))


# FUNCTION ARGUMENT
# def name_concat(name, surname):
#     fullname = surname + " " + name # + is for concatinating 
#     print(fullname)

# name_concat("attah", "iyang") 
# name_concat(surname = "attah", name = "iyang") 

# def name_concat2(name, surname):
#     fullname = surname + " " + name # + is for concatinating 
#     print(fullname)
# user_name = input("please enter your name : ")
# user_surname = input("please enter your surname : ")
# name_concat2(user_surname, user_name)    # POSITIONAL ARGUMENT
# name_concat2(surname = user_surname, name = user_name)  # KEYWORD ARGUMENT


# def name_concat(name, surname, age, sex, mood):
#     fullname = f"My name is {surname} {name} i am  {age} years old {sex} and i feel {mood}."
#     print(fullname)

# user_name = input("please enter your name : ")
# user_surname = input("please enter your surname : ")
# user_age = input("please enter your age : ")
# user_sex = input("please enter your sex : ")
# user_mood = input("please enter your mood : ")

# name_concat(user_surname, user_name, age = user_age, sex = user_age, mood = user_mood)    # POSITIONAL AND KEYWORD AREGUMENTS



def name_concat(name, surname, age, sex, mood):
    for name in names: 
        fullname = f"My name is {surname} {name} i am  {age} years old {sex} and i feel {mood}."
        print(fullname)

names = ["Dele", "Bolu", "Sule", "Bala"]
surnames = ["Momodu", "Ogunse", "Gimba", "Bature"]
ages = [29, 17, 25, 40]
sexes = ["male", "female", "male", "male"]
moods = ["happy", "happy", "indiferent", "just there"]

name_concat(names, )