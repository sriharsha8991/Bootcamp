class myclass:
    def __init__(self):
        self.__internalvariable = 30    # non public variable # private after __

    def public_method(self):
        return 'Public'
    
    def __internalmethod(self):     # non public method # private after __

        return "only to be used internally"
    
obj = myclass()
# print(obj._myclass__internalvariable)
# print(obj._myclass__internalmethod())
# import os
# # print(dir(myclass))
# print(help(os))

import glob

print(glob.glob("**/*.py"))