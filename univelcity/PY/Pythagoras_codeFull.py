print("\nguide to what part of the pythagoras you want to calculate \n\n".center(13),
    "h - Answer the initial question with 'h' to find the hypothenus\n".center(13),
    "o - Answer the initial question with o to find the opposite\n".center(13),
    "a - Answer the initial question with a to find the opposite\n".center(13))

side_find = input("what side of the triangle are you looking for : ")
if (side_find == 'h'):
    print("you are looking for the hypothenus..")
    a = int(input("please input your adjacent value: ")) #allow user input adjacent value on the right angle triangle
    b = int(input("please input your opposite value: ")) #allow user input opposite value on the triangle

    c = int((a**2 + b**2)**0.5)
    print("The Hypothenus value on your triangle is", c)

elif (side_find == 'o'):
    print("you are looking for the Opposite..")
    a = int(input("please input your hypothenus value: ")) #allow user input adjacent value on the right angle triangle
    b = int(input("please input your adjacent value: ")) #allow user input opposite value on the triangle

    c = int((a**2 - b**2)**0.5)
    print("The Opposite value on your triangle is", c)

elif (side_find == 'a'):
    print("you are looking for the adjacent..")
    a = int(input("please input your hypothenus value: ")) #allow user input adjacent value on the right angle triangle
    b = int(input("please input your opposite value: ")) #allow user input opposite value on the triangle

    c = int((a**2 - b**2)**0.5)
    print("The adjacent value on your triangle is", c)
else:
    print("Please take a look at the guide again")

