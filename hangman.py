word = "fenchy"
guessed_letters = []
attempts = 5

while attempts > 0:
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + ''
        else: 
            display += "_"
    
    print("\nword: ", display)

    if "_" not in display:
        print("you guessed the word! shout out to you.")
    

    guess = input("guess a letter: ")

    if guess in guessed_letters:
        print("you've guessed this word already, try something else")
        continue
    if guess in word:
        guessed_letters.append(guess)
        print("correct!")
    else:
        attempts -=1
        print(f"wrong! try again. attempts left: {attempts}")
    if attempts == 0:
        print("Out of attempts, the word was :", word)
