vowel_retract = input("Please enter name : ")
vowel_list = ['a','e','i','o','u']
# length = len(vowel_list)
emptylist =[]
for letters in vowel_retract:
   if letters in vowel_list:
         emptylist.append(letters)
print(emptylist)
# if "a" in vowel_retract:
#     print("Your name contains a vowel")
# elif "e" in vowel_retract:
#     print("Your name contains a vowel")
# elif "i" in vowel_retract:
#     print("Your name contains a vowel")
# elif "o" in vowel_retract:
#     print("Your name contains a vowel")
# elif "u" in vowel_retract:
#     print("Your name contains a vowel")
# else:
#     print("\n There is(are) no vowel(s) in the name")