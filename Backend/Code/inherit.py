class myself: # Parent Class
    def my_details(self):
        return "Hi Im Sriharsha"

class A:
    def m1(self):
        pass
class B:
    def m2(self):
        pass

class myprofession(myself,A): # Child Class
    def my_professional_details(self):
        myintro = super().my_details()
        fun1 = super().m1()
       
        # super().__init__()

        return myintro+" and Im a Data Scientist."
    
obj = myprofession()
print(obj.my_professional_details())

# print(isinstance(obj,B))

print(issubclass(myprofession,myself)) # True Because Myprofession is a sub class of myself

print(issubclass(myself,myprofession))# False Because myself is a superclass of myprofession
    

