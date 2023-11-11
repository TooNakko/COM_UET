import random


def ArrayGenerator():
    ArrayOfNums = [ round(random.random()*10,2), round(random.random()*10,2), round(random.random()*10,2),
                        round(random.random()*10,2), round(random.random()*10,2), round(random.random()*10,2)]
    
    return str(ArrayOfNums).replace('[','').replace(']','')
