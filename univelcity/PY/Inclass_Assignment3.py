# this code is used to find even and odd numbers

# num_detect = int(input("please enter a value : "))
# if ((num_detect % 2) == 0):
#     print("%i is an even number"%(num_detect))
# else:
#     print("%i is an odd number"%(num_detect))
    

#The next block of code is used to find numbers greater and equal to each other

# first_num = int(input("Please enter a number"))           #get the first number
# second_num = int(input("Please enter a second number"))          #get the second number

# if first_num > second_num:
#     #print("%i is greater than %i"%(first_num,second_num)) # if the first number is greater print first number is greater
#     print(f"{first_num} is greater than {second_num}") # if the first number is greater print first number is greater
# elif first_num < second_num:
#     print("%i is less than %i"%(first_num,second_num))    #if the first number is less print it is less
# else:
#     print("%i is equal to %i"%(first_num,second_num))     # print both numbers are equal


# The following program tries to diagnose your medical condition using your symptoms
# symptoms like(headache, vomiting)

symptom1 = 'headache'
symptom2 = 'fever'
symptom3 = 'vomiting'

headache_response = input(f"Do you feel {symptom1} ? respond y/n ")
if headache_response == 'y':                                     #check for headache

    fever_response = input(f"do you feel {symptom2} ? respond y/n ")

    if fever_response == 'y':                 #check for fever

        vomit_response = input(f"do you feel {symptom3} ? respond y/n ")

        if vomit_response == 'y':                                   #check for vomiting 

            print("You have typhoid, please see a doctor!")  

        elif  vomit_response == 'n':                                   #check for vomiting 

            print("You have malaria, please see a doctor!")  

    else:                                                           #No headache

        print("You are stressed, you need to rest") # patient has no headache or fever
                 
else:                                       
    print("You are most likely okay. You can also see a doctor to confirm") # patient has no headache or fever