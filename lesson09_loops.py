#two types of loops
#for loop
import time
bums = ["Le Murr", "Le' Boin", "General Gre Gory", "Shadow Boxer K", "The Cat God" ]
bums[0]

for frauds in bums:
    print("Now Eliminating : ", frauds)
    time.sleep(1.5)


print("All these frauds got cooked")







for i in range(5):
    print("Counting frauds...", i)



fav_word = "six swan"
letter_list = []
for letter in fav_word:
    print(letter, end="")
letter_list.append(letter)
print(letter_list)

count = 0

while count < 5: 
    print(f"Loopin'. We are on loop # {count}.")
    count += 1
    time.sleep(0.5)

print("We have escaped the loop!")

user_input = ""

while user_input != "exit":
    user_input = input("Type 'exit' to escape:")




count = 60
increment = 1

while count > 0:
    count += increment
    increment *= 100000000000000000000000000000000000000000000000000000

    print(count)