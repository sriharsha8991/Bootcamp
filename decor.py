import time as t

def time_it(func):
     def wrapper(*args,**kwargs):
          start = t.time()
          result = func(*args,**kwargs)
          end = t.time()
          execute = (end-start)*1000

          print(func.__name__+" Execution time is "+str(execute)+" milliseconds")
          return result
     return wrapper

@time_it
def squares(nums):
    l = []
    for i in nums:
         l.append(i*i)
    return l

@time_it
def cubes(nums):
    l = []
    for i in nums:
         l.append(i*i*i)
    return l




nums = range(1,100000)

squares(nums)
cubes(nums)

