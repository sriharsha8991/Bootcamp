# # class Dog:
# #     kind = "canine"     # class variable
    

# #     def __init__(self,name):
# #         self.name = name
# #         self.tricks = []

# #     def add_tricks(self,trick):
# #         self.tricks.append(trick)


# # my_dog = Dog("tiger")   # Instance1 or object1 of the Classs Dog
# # sathiks_dog = Dog("shark")   # Instance2 or object2 of the Classs Dog

# # print(my_dog.name)          
# # # print(my_dog.kind)
# # my_dog.add_tricks("swim")

# # print(my_dog.tricks)


# # print(sathiks_dog.name)     
# # # print(sathiks_dog.kind)
# # sathiks_dog.add_tricks("sprint")
# # print(sathiks_dog.tricks)


# class database:
#     purpose = "storage"
#     region = "west"

# db1 = database()
# print(db1.purpose,db1.region)

# db2 = database()
# db2.purpose = "retrieval"
# print(db2.purpose,db2.region)



class Animal:       # Parent class/super class
    def speaks(self):
        print("Animal speaks")

class swimmer:
    def swim(self):
        return "Swimmer swims"
class Dog(Animal,swimmer):              # Child class/subclass
    def bark(self):
        return "Dogs bark"

d1 = Dog()
print(d1.bark())
print(d1.speaks())
print(d1.swim)