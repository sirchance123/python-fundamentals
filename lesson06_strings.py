greeting = "Hello"
name = "skibidi"
print(greeting, name)

# 0 1 2 3 4 
# H e l l o
second_letter = greeting[1]
print(second_letter)

message = greeting + " " + name + "!!!!"
print("Concatenated message:", message)
word = "Super-cali-fragil-istic-expi-ali-docious"
print("First letter:", word[0])
print("Last letter:", word[-1])
print("Range of letters (non-inclusive):", word[6:17])
print(word[:5])
print("Last seven letters:", word[:-7])
print("Step through every second character:", word[::2])
print("Reversed, stepping every third letter:", word[::-3])

country = "Canadaandadnadnadandadnadandadnadadnadadnadadnadadnadnanadaanadadnadadnadadnadadndadnaanadandadnadananadnanaanadnaanadnaanadnaand"
length_of_word = len(country)
print(length_of_word)
phrase = "sP0ng13D006"
print(phrase.upper())
print(phrase.capitalize())
print(phrase.lower())



sentence = "imma goofy goober  RAAHH"
new_sentence = sentence.replace("imma" , "you're")
print(sentence)
print(new_sentence)



name = "skibidi"
age = 67
city = "sigmatown"

print(f"Hello, my name is {name}.  I am {age} years old and live in {city}.")

print(f"Next year, I'll be {age + 1}. My name in uppercase is {name.upper()}.")



#challenge uno
favorite_quote = input("What is your favorite quote? : ")
length_of_quote = len(favorite_quote)
print("Your quote is..." ,length_of_quote , "...characters long, am i right or am i right?")


#challenge drei (german 2)
first_name = input("What is your first name? asking for a friend btw : ")
last_name = input("And what about your last? this is just a random question...prolly : ")

print("YOUR FULL GOVERMENT NAME IS PROBABLY" , last_name ,"," ,first_name)

#challenge dwa (its my lagnuage for 67)
random_word = input("hey so itd be really cool if you just gave me a random word...yknow? : ")
print("AHA I RUINED YOUR WORD!!!" , random_word.upper() , random_word.lower() , random_word[::-1])


