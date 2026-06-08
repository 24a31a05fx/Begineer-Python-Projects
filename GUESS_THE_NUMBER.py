# ================================
#     GUESS THE NUMBER GAME
# ================================

import random

def get_difficulty():
    print("\n" + "="*45)
    print("        🎯 GUESS THE NUMBER GAME")
    print("="*45)
    print("\nChoose Difficulty:")
    print("  1. Easy   → 1 to 10   (10 chances)")
    print("  2. Medium → 1 to 50   (7 chances)")
    print("  3. Hard   → 1 to 100  (5 chances)")
    print("  4. Expert → 1 to 500  (3 chances)")

    while True:
        choice = input("\nEnter your choice (1-4): ").strip()
        if choice == "1":
            return 1, 10, 10, "Easy"
        elif choice == "2":
            return 1, 50, 7, "Medium"
        elif choice == "3":
            return 1, 100, 5, "Hard"
        elif choice == "4":
            return 1, 500, 3, "Expert"
        else:
            print("  ⚠️  Invalid choice. Enter 1 to 4.")


def play_game():
    low, high, max_attempts, level = get_difficulty()
    secret = random.randint(low, high)
    attempts = 0
    guessed = False

    print(f"\n🎮 [{level} Mode] I'm thinking of a number between {low} and {high}.")
    print(f"   You have {max_attempts} chances. Good luck!\n")

    guess_history = []

    while attempts < max_attempts:
        remaining = max_attempts - attempts
        print(f"  ({'❤️ ' * remaining})")

        try:
            guess = int(input(f"  Attempt {attempts + 1}/{max_attempts} → Your guess: "))
        except ValueError:
            print("  ⚠️  Please enter a valid number!\n")
            continue

        if guess < low or guess > high:
            print(f"  ⚠️  Out of range! Guess between {low} and {high}.\n")
            continue

        attempts += 1
        guess_history.append(guess)

        if guess == secret:
            guessed = True
            print("\n" + "🎉" * 20)
            print(f"  ✅ CORRECT! The number was {secret}!")
            print(f"  🏆 You got it in {attempts} attempt(s)!")
            score = calculate_score(attempts, max_attempts, level)
            print(f"  ⭐ Your Score: {score} points")
            print("🎉" * 20)
            break
        elif guess < secret:
            diff = secret - guess
            if diff <= 5:
                print("  🔥 Very Hot! Go a little HIGHER!\n")
            elif diff <= 15:
                print("  ♨️  Warm! Go HIGHER!\n")
            else:
                print("  ❄️  Too LOW! Go much higher!\n")
        else:
            diff = guess - secret
            if diff <= 5:
                print("  🔥 Very Hot! Go a little LOWER!\n")
            elif diff <= 15:
                print("  ♨️  Warm! Go LOWER!\n")
            else:
                print("  ❄️  Too HIGH! Go much lower!\n")

    if not guessed:
        print("\n" + "-"*45)
        print(f"  💀 GAME OVER! You've used all {max_attempts} attempts.")
        print(f"  😢 The number was: {secret}")
        print("-"*45)

    print(f"\n  📋 Your guesses: {guess_history}")


def calculate_score(attempts, max_attempts, level):
    level_bonus = {"Easy": 10, "Medium": 20, "Hard": 40, "Expert": 80}
    base = max_attempts - attempts + 1
    return base * level_bonus[level]


# ================================
#         HIGH SCORE TRACKER
# ================================
high_scores = []

def show_scores():
    if not high_scores:
        print("\n  No scores yet. Play a game first!")
        return
    print("\n" + "="*45)
    print("          🏆 HIGH SCORES")
    print("="*45)
    sorted_scores = sorted(high_scores, reverse=True)
    for i, score in enumerate(sorted_scores[:5], 1):
        print(f"  {i}. {score} points")
    print("="*45)


# ================================
#           MAIN MENU
# ================================
def main():
    print("\n" + "*"*45)
    print("  🎯 WELCOME TO GUESS THE NUMBER GAME! 🎯")
    print("*"*45)

    while True:
        print("\n📋 MAIN MENU:")
        print("  1. Play Game")
        print("  2. View High Scores")
        print("  3. Quit")

        choice = input("\nEnter your choice (1-3): ").strip()

        if choice == "1":
            play_game()
            again = input("\n🔄 Play again? (yes/no): ").strip().lower()
            if again not in ("yes", "y"):
                print("\nThanks for playing! Goodbye! 👋\n")
                break
        elif choice == "2":
            show_scores()
        elif choice == "3":
            print("\nThanks for playing! Goodbye! 👋\n")
            break
        else:
            print("  ⚠️  Invalid choice. Enter 1 to 3.")


if __name__ == "__main__":
    main()


'''
**Guess the Number Game in Python**

This is a command-line based number guessing game developed using Python. The objective of the game is for the player to guess a randomly generated number within a limited number of attempts. The project was designed to practice problem-solving, user interaction, input validation, and game logic implementation.

The game offers multiple difficulty levels, each with a different number range and attempt limit. Based on the selected difficulty, the program generates a random secret number and provides feedback after each guess to help the player move closer to the correct answer.

### Key Features

* Four difficulty levels: Easy, Medium, Hard, and Expert.
* Random number generation using Python's `random` module.
* Limited attempts based on difficulty.
* Hot/Warm/Cold hints based on how close the guess is to the secret number.
* Score calculation system that rewards efficient guessing and harder difficulty levels.
* Guess history tracking.
* High score display functionality.
* Menu-driven user interface.

### How It Works

1. The user selects a difficulty level.
2. Based on the difficulty, the program sets:

   * Number range
   * Maximum attempts
   * Difficulty name
3. A secret number is generated using `random.randint()`.
4. The player enters guesses.
5. The program validates the input and checks whether it is within the allowed range.
6. After each guess, feedback is provided:

   * Very Hot → Very close
   * Warm → Moderately close
   * Too High/Too Low → Far from the target
7. If the user guesses correctly, a score is calculated based on remaining attempts and difficulty level.
8. If all attempts are used, the game reveals the correct number.
9. The user's guesses are displayed at the end of the game.

### Python Concepts Used

* Functions (`get_difficulty`, `play_game`, `calculate_score`, `show_scores`, `main`)
* Random number generation (`random.randint`)
* Lists for storing guess history and scores
* Dictionaries for difficulty-based score bonuses
* Loops (`while`)
* Conditional statements (`if-elif-else`)
* Exception handling (`try-except`) for input validation
* Sorting (`sorted`) for displaying high scores

### Challenges Faced

One challenge was creating meaningful feedback instead of simply telling the player whether the guess was correct or not. This was solved by calculating the difference between the guessed number and the secret number and categorizing it as Hot, Warm, or Cold.

Another challenge was designing the game to support multiple difficulty levels without duplicating code. This was solved by returning the range and attempt limits from a dedicated difficulty-selection function.

### Possible Improvements

* Store high scores permanently using files or a database.
* Add multiplayer mode.
* Introduce timed challenges.
* Build a graphical interface using Tkinter or Pygame.
* Track player statistics across multiple games.

'''