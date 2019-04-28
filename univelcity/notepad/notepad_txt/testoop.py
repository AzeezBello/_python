# try:
#     x = 1/"a"
# except:
#     print("cannot divide int and string")


class Animal:

    status = "alive"
    breaths = True

    def __init__(self, species, genre, sound):
        self.species = species
        self.genre = genre    
        self.sound = sound    