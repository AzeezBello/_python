#MINI SHOPPING CART
import time

 #You may add your own items
item = ["Laptop","T-Shirt","Pants"]

#You may add your own price of your items but make sure you update the program necessarily. 
cost = ["₦ 35600","₦ 2000","₦ 1200"] 

x = []
l = []
print()
for i,j in zip(item,cost):
    print(i,"=",j)
    print()
choice = 'y' or 'n'
count = 0

while choice == 'y' or choice == 'YES' or choice == 'yes' or choice =='Y':
    print()
    user_1 = input("Enter the name of the item which you would like to purchase : ")
    print()    
    user_2 = int(input("Enter the cost of the item which you would like to purchase : {} ".format("₦")))
    print()
    if user_2 == 35600 or user_2 == 2000 or user_2 == 1200:
        l.append(user_2)
    else:
        print()
        print("TYPE THE EXACT AMOUNT.")
        time.sleep(5)
        break
    if user_1 in item:
        x.append(user_1)
        print()
        print(user_1,"has been added to your cart.")
        print()
        count += 1
    else:
        print()
        print("Item not found.Try restarting the app.")
    choice = input("Do you want to add any other item to your cart :--->[Y/N] ")

while choice == 'n' or choice == 'no' or choice == 'NO' or choice == 'N':
    print()
    print("There are",count,"items in your cart")
    print()
    print("Total : {}".format("₦"),sum(l))
    print()
    print("Thank You for choosing our store we hope to see you soon")
    break