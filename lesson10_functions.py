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


def double_sequencer(number, time):
    sequence.