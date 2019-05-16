# TERNARY OPERATOR

# user_input = input("please enter your name in CAPS")
# name = user_input if user_input.isupper() else "input was not upper case"
# print(name)

score = int(input("please enter your student score : "))

status = "Qualified" if score >= 60 else "Not qualified"

print(status)

student_is_qualified = True if score >= 60 else False

if student_is_qualified:
    print("\nsending mail to student\n")
    print("Content: you have qualified for admision please visit our page to continue your registration")
    
