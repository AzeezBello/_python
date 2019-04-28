##first_item = input("Please enter first item name :")
##item1_price = int(input("please enter first item Price : "))
##item1_qty = int(input("Please enter first item Qty :"))
##
##
##second_item = input("Please enter second item name :")
##item2_price = int(input("please enter second item Price : "))
##item2_qty = int(input("Please enter second item Qty :"))
##
##third_item = input("Please enter third item name :")
##item3_price = int(input("please enter third item Price : "))
##item3_qty = int(input("Please enter third item Qty :"))
##
##
##fourth_item = input("Please enter fourth item name :")
##item4_price = int(input("please enter fourth item Price : "))
##item4_qty = int(input("Please enter fourth item Qty :"))
##
##total_stock = (item1_price * item1_qty) + (item2_price * item2_qty) + (item3_price * item3_qty) + (item4_price * item4_qty)
##print (total_stock)


first_item = "Nike"
item1_price = 23
item1_qty = 45

second_item = "Shoes"
item2_price = 300
item2_qty = 4

third_item = "Adidas"
item3_price = 350
item3_qty = 12

fourth_item = "Puma"
item4_price = 250
item4_qty = 3

total_stock = ( item1_price * item1_qty) + ( item2_price * item2_qty) + (item3_price * item3_qty)+ (item4_price * item4_qty)



print("Name".center(13), "Price".center(13), "qty".center(13), "Total".center(13), "\n")

print(first_item.center(13), str(item1_price).center(13),str(item1_qty).center(13), str(item1_price * item1_qty).center(13))

print(second_item.center(13), str(item2_price).center(13) , str(item2_qty).center(13), str(item2_price * item2_qty).center(13))

print(third_item.center(13), str(item3_price).center(13) , str(item3_qty).center(13), str(item3_price * item3_qty).center(13))

print(fourth_item.center(13), str(item4_price).center(13) , str(item4_qty).center(13), str(item4_price * item4_qty).center(13))

print(total_stock)
