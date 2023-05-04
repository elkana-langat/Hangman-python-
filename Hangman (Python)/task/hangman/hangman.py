import random
import string

games_won = 0
games_lost = 0
while True:
    print("H A N G M A N")
    print('Type "play" to play the game, "results" to show the scoreboard, and '
          '"exit" to quit:')

    action = input()
    if action == "play":
        words = ["python", "java", "swift", "javascript"]
        chosen_word = random.choice(words)
        hidden_word = "-" * len(chosen_word)
        attempts = 8
        guessed_letters = []

        while attempts > 0:
            print()
            print(hidden_word)
            print("Input a letter:")
            guess = input()
            length = len(guess)

            if length != 1:
                print("Please, input a single letter.")
            elif length == 1 and guess not in string.ascii_lowercase:
                print("Please, enter a lowercase letter from the English alphabet.")
            elif length == 1 and guess in string.ascii_lowercase:
                if guess in guessed_letters:
                    print("You've already guessed this letter.")
                elif guess not in guessed_letters:
                    guessed_letters.append(guess)
                    if guess in chosen_word:
                        for i in range(len(chosen_word)):
                            if chosen_word[i] == guess and hidden_word[i] == "-":
                                hidden_word = hidden_word[:i] + guess + hidden_word[i + 1:]
                    else:
                        print("That letter doesn't appear in the word.")
                        attempts -= 1

                    if hidden_word == chosen_word:
                        print(f"You guessed the word {hidden_word}!")
                        print("You survived!")
                        games_won += 1
                        break

        if attempts == 0 and hidden_word == chosen_word:
            print(f"You guessed the word {hidden_word}!")
            print("You survived!")
            games_won += 1
        elif attempts == 0 and hidden_word != chosen_word:
            print("You lost!")
            games_lost += 1
    elif action == "results":
        print(f"You won: {games_won} times.")
        print(f"You lost: {games_lost} times.")
    elif action == "exit":
        break
