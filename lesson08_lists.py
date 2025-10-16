animals = ["penguin" , "armadillo" , "R. Ost"]
print(animals)
print(animals[-1])



animals[0] = "Le' Boin"
print(animals)

animals.append("Teacher Bun Bun")
print(animals)

animals.insert(3, "Metal Face")
print(animals)
animals.insert(5, "Le Murr")
print(animals)
animals.remove("armadillo")
print(animals)
animals.pop()
print(animals)

empty_list = []




nums = [5, 2, 6, 7, 9, 3, 4, 1, 0, 8]

print("length", len(nums))

print("min", min(nums))
print("max", max(nums))
print("sum", sum(nums))

nums.sort()
print(nums)

animals.sort()
print(animals)

if "Le' Boin" in animals:
    print("Yeah hes there")
else:
    print("Lil buddy is NOT there")


new_list = [1, 2, 4]
copied_list = new_list.copy()
copied_list.append(5)
print(new_list)
print(copied_list)


matrix = [ 
     [1], 
     [2, 3], 
     [4,5], 
     [6, 7]
       ]


print(matrix[2])


#cfhallene uno


challenge_nums = [1, 2, 3, 4, 5, 6 ]
print(challenge_nums)
x = int(input("Enter a number to replace the third number in the list of numbers"))




#challengeihassif dos

shoppin = []
milk = "milk"
cheese = "cheese"
banana = "potassuim inducing big curved yellow pill"
egg = "center of life in a chickens pill"
shoppin.append(milk)
shoppin.append(cheese)
shoppin.append(banana)

shoppin.insert(2, egg)

shoppin.remove(cheese)
print(shoppin)