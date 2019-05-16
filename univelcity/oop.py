# class Person:#class declaration
#     mouth = 1
#     hands = 2
#     legs  = 2

#     def __init__(self, eye_colour, skin_colour):#initializer for instance variables
#         self.eye_colour = eye_colour
#         self.skin_colour = skin_colour

#     def walk(self):
#         print("Walking on foot")

# class Politician(Person):#class declaration
#     run_for_office = True

#     def walk(self):
#         print("Too fresh, Flying private .")

# saraki = Politician("grey", "dark")
# ade = Person("brown", "Pale")#an object ( instance of a class)
# bolu = Person("red", "black")#an object ( instance of a class)
# bola = Person("blue", "extra black")#an object ( instance of a class)

def adder(x,y): # Function
    return x+y


class Data:

    def __init__(self, main_data):
        self.main_data = main_data
        self.__length = len(main_data)
        self.unique = str(set(main_data))
        self.mean = self.__avg()

    def __avg(self):
        mean = sum(self.main_data)/self.__length
        return mean
    
    def get_len(self): #getter method
        return (self.__length)

    def set_len(self):
        self.__length = 12

rand = Data([1,2,2,3,3,3,4,5100000, 234])
print(rand.mean)
print(rand.get_len())
rand.__avg()