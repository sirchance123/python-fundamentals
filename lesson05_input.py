name = input("Enter your name: ")
print("Hello", name)

age = int(input("Enter your age :"))
print(type(age))

age_number = int(age)
print("Next year, you will be:", age_number + 1)
print(type(age))

height = float(input("Enter your height in meters: "))
print("You are", height, "meters tall.")

#challenge
color = input("Enter Your Favorite Color :")
print(color)

#challenge 2
number_1 = int(input("Give me a random number :"))
number_2 = int(input("Give me a second number :"))
print("I shall now add them together...and you get..." , number_1 + number_2)
#woah i actually did it. this lowkey tuff ngl

#challenge 3
import math
diameter = int(input("Give me a random diameter for a circle :"))
radius = diameter / 2
area = radius ** 2
circle_area = area * math.pi
print("The area of a circle with the diameter of your choice is...", circle_area)

#challenge 4
import random
custom_dice_roll = int(input("Name how many sides any dice has :"))
print("You rolled...", random.randint(1, custom_dice_roll))


