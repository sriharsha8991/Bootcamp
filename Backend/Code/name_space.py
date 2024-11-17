global_var = "Im Global var"

class Example:
    class_var = "Im Class var"
    def __init__(self,name,age) :
        self.name = name
        self.a = age

#     def method(self):
#         global local_var 
#         local_var = "Im local"
#         print(local_var)      # Local Scope
#         print(self.class_var) # Class Level Scope
#         print(global_var)     # For Global Scope
    
#     print(local_var)
# print(local_var)

ex = Example("Sri",29)
print(ex.name)
print(ex.a)

