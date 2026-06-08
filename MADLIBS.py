# =================================
#        MAD LIBS GAME IN PYTHON
# =================================

import random


def play_madlibs(story_name, template, blanks):
    """Ask for words from the user and insert them into the story."""
    print("\n" + "=" * 45)
    print(f"       Story: {story_name}")
    print("=" * 45)
    print("Fill in the blanks to create your story!\n")

    # Store the user's answers in a dictionary.
    # Example: {"animal": "cat", "food": "pizza"}
    answers = {}
    for blank in blanks:
        prompt = blank.replace("_", " ")
        answer = input(f"  Enter a {prompt}: ").strip()
        answers[blank] = answer

    # Replace each placeholder in the story with the user's answer.
    # Example: {animal} is replaced with the answer for "animal".
    story = template
    for blank, value in answers.items():
        story = story.replace(f"{{{blank}}}", value)

    print("\n" + "-" * 45)
    print("HERE IS YOUR MAD LIBS STORY:")
    print("-" * 45)
    print(f"\n{story}\n")
    print("=" * 45)


# ---- STORY 1 ----
story1_name = "The Crazy Adventure"
story1_template = (
    "One day, a {adjective} {noun} decided to go on a trip to {place}.\n"
    "On the way, they found a {adjective2} {animal} who could {verb}.\n"
    "Together, they ate {number} plates of {food} and became best friends!\n"
    "Everyone in {place} cheered and said it was the most {adjective3} day ever!"
)
story1_blanks = [
    "adjective", "noun", "place",
    "adjective2", "animal", "verb",
    "number", "food", "adjective3"
]


# ---- STORY 2 ----
story2_name = "My Weird School Day"
story2_template = (
    "Today at school, my teacher {name} walked in wearing a {adjective} {clothing}.\n"
    "She told us to open our {noun} and start {verb}ing immediately.\n"
    "Suddenly, a {animal} ran into the classroom and ate the {food}!\n"
    "Everyone screamed '{exclamation}!' and ran to {place}.\n"
    "It was the most {adjective2} school day ever!"
)
story2_blanks = [
    "name", "adjective", "clothing",
    "noun", "verb", "animal",
    "food", "exclamation", "place", "adjective2"
]


# ---- STORY 3 ----
story3_name = "Space Explorer"
story3_template = (
    "Astronaut {name} blasted off to planet {made_up_planet} in a {adjective} rocket.\n"
    "The aliens there had {number} eyes and loved to {verb} all day.\n"
    "They offered {name} a bowl of {food}, which tasted like {another_food}.\n"
    "Before leaving, {name} gave them a {noun} as a gift.\n"
    "The aliens were so {adjective2}, they danced the {dance_move}!"
)
story3_blanks = [
    "name", "made_up_planet", "adjective",
    "number", "verb", "food",
    "another_food", "noun", "adjective2", "dance_move"
]


# Put all stories into one list so the menu can show them easily.
stories = [
    (story1_name, story1_template, story1_blanks),
    (story2_name, story2_template, story2_blanks),
    (story3_name, story3_template, story3_blanks),
]


# =================================
#             MAIN MENU
# =================================
def main():
    """Show the menu and keep the game running until the user quits."""
    print("\n" + "*" * 45)
    print("   WELCOME TO MAD LIBS PYTHON GAME!")
    print("*" * 45)

    while True:
        # Display the story menu.
        print("\nChoose a story:")
        for i, (name, _, _) in enumerate(stories, 1):
            print(f"  {i}. {name}")
        print("  4. Random Story")
        print("  5. Quit")

        choice = input("\nEnter your choice (1-5): ").strip()

        # Run the story selected by the user.
        if choice in ("1", "2", "3"):
            story_index = int(choice) - 1
            play_madlibs(*stories[story_index])
        elif choice == "4":
            play_madlibs(*random.choice(stories))
        elif choice == "5":
            print("\nThanks for playing Mad Libs! Goodbye!\n")
            break
        else:
            print("  Invalid choice. Please enter 1 to 5.")
            continue

        # Ask if the user wants to play another round.
        again = input("\nPlay again? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("\nThanks for playing Mad Libs! Goodbye!\n")
            break


if __name__ == "__main__":
    main()


'''
**Mad Libs Game in Python**

This is a command-line based Mad Libs game developed using Python. The purpose of the project is to generate funny and interactive stories by taking user inputs and inserting them into predefined story templates.

The application contains multiple story templates, each having placeholders such as nouns, verbs, adjectives, places, and food items. When a user selects a story, the program prompts them to fill in the required blanks. These inputs are then dynamically inserted into the template to create a unique story.

I implemented the project using Python functions, lists, dictionaries, loops, and string manipulation techniques.

### Key Features

* Multiple story options for users.
* Random story selection using Python's `random` module.
* Interactive menu-driven interface.
* Dynamic placeholder replacement using dictionaries.
* Replay functionality that allows users to generate multiple stories without restarting the program.

### How It Works

1. The program displays a menu of available stories.
2. The user selects a story or chooses a random one.
3. The program asks for words corresponding to different categories such as adjective, noun, verb, etc.
4. Inputs are stored in a dictionary where the placeholder name is the key and the user's input is the value.
5. The program replaces placeholders in the story template with the provided inputs.
6. The completed story is displayed to the user.

### Python Concepts Used

* Functions (`play_madlibs`, `main`)
* Dictionaries for storing user inputs
* Lists and tuples for organizing story data
* Loops (`for`, `while`)
* Conditional statements (`if-elif-else`)
* String replacement using `.replace()`
* Randomization using `random.choice()`

### Challenges Faced

One challenge was designing a reusable function that could work for different story templates without rewriting code. This was solved by storing story data separately and passing it as arguments to a common function.

### Possible Improvements

* Create a graphical user interface using Tkinter.
* Save generated stories to a text file.
* Add difficulty levels and more story categories.
* Allow users to create and save their own story templates.


'''