# class Grandparent:
#     height = 170
#     satiety = 100
#     age = 60
#
# class Parent(Grandparent):
#     age = 40
#
# class Child(Parent):
#     height = 50
#     def __init__(self):
#         print(self.height)
#         print(self.satiety)
#         print(self.age)
#
# nick = Child()

class Grandparent:
    def about(self):
        print("I am Grandparent")

    def about_myself(self):
        print("I am Grandparent")


class Parent(Grandparent):
    def about_myself(self):
        print("I am Parent")

class Child(Parent):
    def __init__(self):
        super().about()
        super().about_myself()

kate = Child()
