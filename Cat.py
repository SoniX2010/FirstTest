class Animal:
    print("Мяу")
    def __init__(self,height = 30):
        self.height = height
        self.type = ("Cat")
        self.owner = ("Daniil")


    def printHeight(self):
        print(self.height)


    def printType(self):
        print(self.type)

    def printOwner(self):
        print(self.owner)




Anfisa = Animal(height=40)
Anfisa.printHeight()
Anfisa.printType()
Anfisa.printOwner()
