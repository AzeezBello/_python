shopping_cart = []
shopping_cart_price = []

while True:
    product_input = input("place your product in the cart:")
    product_price = int(input("Enter the price of your product:"))

    shopping_cart.append(product_input)                #adds a new product to the product list
    shopping_cart_price.append(product_price)          #adds a new price to the price list

    if product_input == "end" and product_price == 0:
        shopping_cart.pop()                            #removes "end" as a member of the list
        shopping_cart_price.pop()
        Total_shopping_price = sum(shopping_cart_price)

        print("The list of product in your cart are:",shopping_cart)
        print("The price list of your items is:",shopping_cart_price)
        print("you have",len(shopping_cart),"product in your cart")
        print("Your are paying a total of ",Total_shopping_price,"dollars")
        break    
    
#PROGRAM TO GIVE OPTION ON REMOVING FROM THE LIST
Request_to_remove = input("do you want to remove any item?")
if Request_to_remove == "yes":
    item_to_remove = input("Select an item to remove: ") 
    if item_to_remove in shopping_cart:
        shopping_cart.remove(item_to_remove) 
        print("The new list of product in your cart are:",shopping_cart)  
        print("you have",len(shopping_cart),"product in your cart") 
        print("Your total new price is ",Total_shopping_price,"dollars")
    else:
        print("This item is not in your list")    
else:
    print("The list of product in your cart are:",shopping_cart)
    print("The price list of your items is:",shopping_cart_price)
    print("you have",len(shopping_cart),"product in your cart")
    print("Your are paying a total of ",Total_shopping_price,"dollars") 
Collapse

