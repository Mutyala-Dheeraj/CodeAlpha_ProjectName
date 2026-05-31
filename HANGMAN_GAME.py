import random

# List of predefined words
words = ["python", "coding", "laptop", "gaming", "school"]

# Randomly choose a word
secret_word = random.choice(words)

# Create blank spaces for the word
guessed_word = ["_"] * len(secret_word)

# Store guessed letters
guessed_letters = []

# Number of incorrect attempts allowed
attempts = 6

print("===================================")
print("        HANGMAN GAME ")
print("===================================")

# Main game loop
while attempts > 0 and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Incorrect Attempts Left:", attempts)
    print("Guessed Letters:", guessed_letters)

    # Take user input
    guess = input("Enter a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("⚠ You already guessed that letter!")

    else:
        guessed_letters.append(guess)

        # Check if guess is correct
        if guess in secret_word:
            print(" Correct Guess!")

            # Reveal the guessed letter in the word
            for index in range(len(secret_word)):
                if secret_word[index] == guess:
                    guessed_word[index] = guess

        else:
            print("Wrong Guess!")
            attempts -= 1

# Result
print("\n----------------------------------")

if "_" not in guessed_word:
    print("Congratulations! You won!")
    print("The word was:", secret_word)

else:
    print(" Game Over!")
    print("The correct word was:", secret_word)

print("----------------------------------")