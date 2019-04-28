#LISTS

# students = ["azeez", "gozie", "abibat", "shayo", "samuel", "di'ja", "kunle", "awele"]
# print(type(students))
# print((students))

# students2 = list("azeez")
# print(type(students2))
# print((students2))

# shopping_cart = ["apple", "coca cola", "Soap", "chicken", "chicken", "chicken"]

# print("Original", (shopping_cart))
# #indexing  list
# print(len(shopping_cart))
# print(shopping_cart[len(shopping_cart)-1])
# print("Before append",len(shopping_cart))

# shopping_cart.append("pot")
# print(shopping_cart)
# print("after append", len(shopping_cart))

# shopping_cart.remove(shopping_cart[0])
# print("after remove", len(shopping_cart))
# print("after remove", (shopping_cart))

# duplicate_cart = shopping_cart.copy()
# print("duplicate_cart", len(duplicate_cart))
# print("duplicate_cart", (duplicate_cart))

# shopping_cart.clear()
# print("after Clear", len(shopping_cart))
# print("after Clear", (shopping_cart))

# print("duplicate_cart", len(duplicate_cart))
# print("duplicate_cart", (duplicate_cart))

# print(duplicate_cart.count("pot"))

# print(duplicate_cart.reverse())
# print(duplicate_cart)
# duplicate_cart.pop(3)
# duplicate_cart.sort()
# print(duplicate_cart)

# hertero_list = [1,"hello", print, list, int, str, bool, True]
# hertero_list[2]("i am a boy")
# print("i am a boy")

# femi_print = print

# femi_print("this is the new type of print")


# numbers = [number *10 for number in range(20)]

# print(numbers)
# pt = print
# numbers = []

# for number in range(100):
#     numbers.append(number)
#     pt(numbers, "\n")
# print(numbers)

# print(shopping_cart[-1])

# shopping_cart = ["apple", "coca cola", "Soap", "chicken", "pork", "ham", "polony"]

# print(shopping_cart[::2])

# shopping_cart[::] = [23,45,23,53]
# print(shopping_cart)

# shopping_cart = ["apple", "coca cola", "Soap", "chicken", "pork", "ham", "polony", ["screwdriver", "wrench", "plier"] ]

# print(shopping_cart[-1][2])

#TUPLES
# new_tuple  = ("apple", "coca cola", "Soap", "chicken", "pork", "ham", "polony")

# #new_tuple[0] = "orange"

# print(new_tuple[0])
# print(new_tuple[::-1])
# print(new_tuple)

# _dict = {"key": "value","key2": "value"}

# MLB_team = {
#      'Colorado' : 'Rockies',
#      'Boston'   : 'Red Sox',
#      'Minnesota': 'Twins',
#      'Milwaukee': 'Brewers',
#      'Seattle'  : 'Mariners'
#  }
# print(MLB_team)

# print(MLB_team['Boston'])

oxford = {
    "noun": "Name of person animal place or thing",
    "pronoun": "Used instead of a noun",
    "verb": "Action word",
    "adjective": "describes a noun"
}

print(oxford['adjective'])

# while True:
#     user_in = input("Enter a word to search : ")

#     print(oxford[user_in])

# print(oxford["pronoun"])

# _class = {
#     "chidi":["sleeping", "eating", "travelling"],
#     "tolu":["coding", "reading complex stuff", "writing advanced code"],
#     "femi":["speaking big grammar", "lightening class mood", "teaching complex math",  "analysing grammar"],
#     "omotayo":[ "drinking sweet stuff", "chowing biscuit", "pressing phone"],
#     "Mr tayo": ["Selling insurance", "Giving updates", "Encyclopedia"],
#     "shade" : ["accounting", "coming late", "shalaye'ing"],
#     "attah": ["being cool", "being calm", "being collected", "being awesome", "eating affang"]
# }

# for item in _class["Mr tayo"]:
#     print(item)

# _class = {
#     "chidi":{
#         "surname": "Igbo",
#         "hobbies":["sleeping", "eating", "travelling"],
#         "phone": "0804465862"
#         },
#     "tolu":{
#         "surname": "Igbo",
#         "hobbies":["sleeping", "eating", "travelling"],
#         "phone": "0804465862"
#         },
#     "femi":["speaking big grammar", "lightening class mood", "teaching complex math",  "analysing grammar"],
#     "omotayo":[ "drinking sweet stuff", "chowing biscuit", "pressing phone"],
#     "Mr tayo": ["Selling insurance", "Giving updates", "Encyclopedia"],
#     "shade" : ["accounting", "coming late", "shalaye'ing"],
#     "attah": ["being cool", "being calm", "being collected", "being awesome", "eating affang"]
# }

# print(_class["chidi"]["hobbies"][-1])
#creating dictionaries VIA TUPLES

# print(_class["chidi"])
# print((_class["chidi"]))
# print(type(_class["chidi"]))

# for_conversion = [("happy", ["pleased", "excited"]),("angry", "vexed"),("run", "sare"), ("fall down", "subu"), ("shayo", "create joy")]

# synonyms = dict(for_conversion)

# print(synonyms)
#CREATING DICT VIA VARIABLES
# products = dict(
#     beans= 100,
#     rice=200,
#     garri= 300,
#     meat= 400,
#     poundo= 150,
#     pork= 250
#  )

# cart = []
# bill = 0

# while True:
#     consumer_response = input("Please what do you intend to do : ")

#     if consumer_response == "add":
#         for key in products:
#             print(key, "₦" + str(products[key]))

#         consumer_response = input("Please what do you intend to add to cart : ")

#         cart.append(consumer_response)
#         print("Your cart now contains ", cart)
    
#     elif consumer_response == "bill":
#         bill = 0
#         for item in cart:
#             bill += products[item]

#         print("Your current bill stands at : ", bill)
    
#     if consumer_response == "admin":
#         print("Welcome admin \n")

#         print("Enter D for delete and A for add \n")

#         admin_response = input("Please what do you intend to do : ")

#         if admin_response == "A":
#             new_item = input("Please enter the product name : ")

#             price = input("Please enter the product price : ")

#             products[new_item] = int(price)


#Sets

# new_set = {"<val1>", "<val2>", "<val3>", (1,2,3)}
# _list = ["<val1>", "<val2>", "<val3>", (1,2,3)]
# new_set = set(_list)

# _tuple = (1,2,3)
# new_set = set(_tuple)
# print(12 in new_set)

# _string = "Atiku abubakar"
# new_set = set(_string)

# print(len(new_set))
# print(len(_string))

#lexical richness
# from speech_file import speech_text 

# words = speech_text

# tokenized_words = words.split(" ")
# unique = set(tokenized_words)

# diversity = len(unique)/len(tokenized_words)
# diversity_percent = diversity * 100
# print(diversity_percent)
