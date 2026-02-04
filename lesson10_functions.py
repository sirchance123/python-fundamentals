print("function (Procedures)")

print("\nExample 1")
def say_hi():
    print("Hi")

def say_bye():
    print("bye")

say_hi()
say_hi()
say_hi()
say_hi()
say_bye()
say_bye()
say_bye()
say_bye()

print("\nExample 2")

def express_this(e):
    return e

expression = express_this(1 +2 )
print(expression)
expression2 = express_this(45 * 6)
print(expression2)

def greeter(n):
    return f"HI {n}!"

first = greeter("jojo")
second = greeter("slumper")
third = greeter("im not sure what the point of this is")

print(first, second, third)








def is_far(distance):
    if distance >= 100:
        return "That's far"
    elif distance < 100 and distance > 20:
        return "That's not too far"
    elif distance < 20 and distance > 0:
        return "That's nearby"
    else:
        return "error"
print(is_far(-1))







#challenge1
#psuedocode part thing idk man.  this was wrong but it helped me outline.
#def challenge1(x, y):
    #print(5 + 7)
#print(challenge1)
#def challenge1(x, y):
    #print(5 - 7)
#print(challenge1)
#def challenge1(x, y):
    #print(5 / 7)
#print(challenge1)
#def challenge1(x, y):
    #print(5 * 7)
#print(challenge1)


def challenge1(x):
    return x
challenge = challenge1(5 + 7)
print(challenge)

def challenge1(x):
    return x
challlenge = challenge1(5 - 7)
print(challlenge)

def challenge1(x):
    return x
challllenge = challenge1(5 / 7)
print(challllenge)

def challenge1(x):
    return x
challlllenge = challenge1(5 * 7)
print(challlllenge)




#challengedrei
#pseudo code stuff again idk man 
#def average(y):
    #return y
#average challenge = average((5 + 10 + 350)/ 3)
#print(average challenge)








def average(y):
    return(y)

averagechallenge = average((5 + 10 + 350) / 3)
print(averagechallenge)



#challenge 3
#def even(z)
    #if z % 2 :
        #return "even":
    #elif z % 3:
        #return "odd"
#print(even(z))

def even(z):
    if z % 2:
        return "odd";
    elif z % 3:
        return "even"
print(even(2))


#challenge 4.  I dont expect myself to get this one correct but I will try nonetheless.
#psuedocode part or something.  Still dont get it but whatever.
#def analyze_word(w):
    #for letter in analyze_word("wordgoeshere"):
        #letter = [list of each letter]
    #if letter has vowel:
        #vowelcount = (vowelcount + 1);
    #elif:
        #consonatcount = (consonantcount + 1)
    #return analyze_word(w)
#print("This word has ", consonatcount, "consonats, and ", vowelcount, "vowels.  ")
#i feel i did this very wrong and I have no idea how to convert this to actual python.  I hope my idea was close and it counts as trying.  Because well, I did try.  