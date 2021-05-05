import random
def rand(min=0   , max=100  ):
    if(min>max):
        return "minimum cannot be bigger than max"
    if(max<0):
        return "maxmum cannot be smaller than zero"
    num =min+ random.random()*max
    return num
print(rand(0,50))