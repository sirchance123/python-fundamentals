#libraries are like stuff that hold stuff (i think.  i lowkey dont know)
import math
print(math.sqrt(25))
print(math.ceil(4.2))
print(math.floor(4.8))
print(math.pow(2, 5))
print(math.pi)

#Psuedorandom number generator.  start with a random number. that number = seed
random = math.pi

psuedo = 718302
part1 = psuedo - random




print("------\n\n")


seed = 12.4444
step1 = seed / 6.7
step2 = step1 - 800
step3 = step2 + 180843
step4 = step3 % 10
result = math.floor(step4)
print(result)





import random
print(random.randint(1, 7))
print(random.random())
print(random.choice(["egg", "milk", "cheese"]))
my_fav = ["egg", "milk", "cheese"]
print(random.choice(my_fav))
random.shuffle(my_fav)
print(my_fav)




#challenge 1
diameter = 14
radius = diameter / 2
circle_area = (radius ** 2) * math.pi
print(circle_area)


#challenge 2
die_roll = random.randint(1, 6)
print("You dice roll is...", die_roll)
