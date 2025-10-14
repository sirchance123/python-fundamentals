num = 10 
if num == 10: 
    print("Your number is equal to 10")

num2 = 12
print(num2 <= 12)
if num2 <= 12:
    print("Your number is less than or equal to 12")
else: 
    print("Your number is greater than 12")

temperature = 62
if temperature > 80: 
    print("It's hot!")
elif temperature >= 60:
    print("It's nice.")
else:
    print("It's cold!")



x = 20
y = 20

if x == y:
    print("x is equal to y")
elif x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else: 
    print("error")


age = 17
has_permission = True

if age >= 17 and has_permission:
    print("You can drive")
else:
    print("You can NOT drive")



print("--- Using 'or' --- ")
day = "Monday"

if day == "Saturday" or  day == "Sunday":
    print("It's the weekend!")
elif day == "Monday" or day == "Tuesday":
    print("It's Monday or Tuesday")
else:
    print("It's Wed,Thur, or Fri")

if day is not "Monday":
    print("Its not monday")