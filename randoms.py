"""
 x = 1
while x < 10:
    print(x)
    if x == 5:
        print("stop")
        break
    x+=1
"""
#===== program 2 ===
"""
animals = ["cat", "giraffe", "lion", "leopard", "mouse"]
for animal in animals:
  if animal[0] == "l":
    continue
  print(animal)


#==== program 3 ====
"""
"""
ages = [12, 16, 17, 43, 46,55,78]
for age in ages:
    if age < 18:
        continue
    print(age)
"""

#program 4:
"""day_number = 1
while day_number <= 7:
    if day_number == 4:
        day_number+= 1
        continue
    print(day_number, "turn on the lights")
    day_number+=1
"""
""""
products = ['ball', 'gloves']
colors = ['red', 'blue']
for i in products :
  for j in colors:
    print(j, i)
"""    

"""
a = int(input('enter the first number: '))
b = int(input('enter the second number: '))

def add(a,b):
    return a + b
result = add(a, b)
print(result)
"""
""""name = input("enter your name: ")
def personal_greet(name): 
  print("Hello", name)
  print("Have a great day")
personal_greet(name)
"""

#BODY MASS INDEX
"""
#passing a boolean as an argument in a function
books = ['oliver twist', 'Ralia the sugar girl', 'chike and the river', 'animal farm']
book = 'animal farm'
def book_in_library_books (books, book):
    return book in books
print(book_in_library_books(books, book))
"""
'''
cart = {
    "brand" : input("enter brand name:"),
    "model" : input("enter model: ")
    
}
print("model" in cart)
info_keys = cart.keys()
info_values = cart.values()
print(info_keys)
print(info_values)
'''
''''
tags=['fitness', 'travel', 'food', 'hotels']
hashtag = [ x for x in tags if x[0] == "f"]

print(hashtag)
'''
''''
sports = ["Football", "Basketball", "Tennis", "Golf", "Volleyball"]
group = [x for x in sports if "ball" in x]

print(group)
'''
''''
price = input()
try:
    price_value = int(price)
except ValueError:
    print('error')
'''
word = "manipulate"
guessed_letters = []
attempts = 6

print("Welcome to Hangman!")

while attempts > 0:
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    if "_" not in display:
        print("🎉 You guessed the word!")
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    if guess in word:
        guessed_letters.append(guess)
        print("Correct!")
    else:
        attempts -= 1
        print("Wrong! Attempts left:", attempts)

if attempts == 0:
    print("💀 Game over! The word was:", word)