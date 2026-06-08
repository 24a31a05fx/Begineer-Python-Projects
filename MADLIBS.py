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
