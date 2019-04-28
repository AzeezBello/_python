
# class ShoppingCart(object):
#     # Creates shopping cart objects for users of our fine website.
#     items_in_cart = {}
#     def __init__(self, customer_name):
#         self.customer_name = customer_name

#     def add_item(self, product, price):
#         # Add product to the cart.
#         if not product in self.items_in_cart:
#             self.items_in_cart[product] = price
#             print( product + " added.")
#         else:
#             print(product + " is already in the cart.")

#     def remove_item(self, product):
#         # Remove product from the cart
#         if product in self.items_in_cart:
#             del self.items_in_cart[product]
#             print(product + " removed.")
#         else:
#             print(product + " is not in the cart.")
    
#     def categories(self, category):
#         file = open ('category.txt' , 'r')
#         for x in file:
#             category = x.split(" ") 
#             return category  
    
# def product_list():
#     file = open ('product.txt' , 'r')
#     for x in file:
#         category = x.split(" ") 
#         return category  

#     pass

def categories():
    file = open ('category.txt' , 'r')
    for x in file:
        category = x.split(" ") 
        print(type(category))
        print(category)

categories()



# def customer_name( ):
#     customer_name = input("Enter your Name:")

# def add_item(product, price):
#     # Add product to the cart.
#     if  product not in items_in_cart:
#         items_in_cart[product] = price
#         print( product + " added.")
#     else:
#         print(product + " is already in the cart.")

# def remove_item(product):
#     # Remove product from the cart.
#     if product in items_in_cart:
#         del items_in_cart[product]
#         print(product + " removed.")
#     else:
#         print(product + " is not in the cart.")



# items_in_cart = ["Laptop","T-Shirt","Pants"]
# price = ["₦ 35600","₦ 2000","₦ 1200"]




# print("welcome to my Shop, Pls no window shopping")
# customer_name()
# print("what do you want to do ? :---->[add/remove]" )
# action = input()

# if action == "add":
#     product =  input("Enter Product Name: ")
#     price = input("Enter Product Price (₦): ")
#     add_item(product, price)

# elif action == "remove":
#     remove_item(product)
    
















