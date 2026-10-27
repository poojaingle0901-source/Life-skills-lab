# A collection of daily motivation thoughts


QUOTES = [
    "Small steps every day lead to big changes.",
    "Believe you can, and you are halfway there. - Theodore Roosevelt",
    "It always seems impossible until it is done. - Nelson Mandela",
    "Great things are done by a series of small things brought together. - Vincent van Gogh",
    "Your future is created by what you do today, not tomorrow."
]

DAILY_TASKS = [
    "Write down one thing you are grateful for.",
    "Spend 10 minutes learning something new.",
    "Take a short break and stretch.",
    "Organize one small part of your workspace.",
    "Help someone with a kind action."
]


def clear_screen():
    """Clears the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def show_quote():
    """Displays a randomly selected motivational quote."""
    print("\nToday's thought:")
    print(random.choice(QUOTES))


def show_task():
    """Suggests one small positive task for today."""
    print("\nYour small task for today:")
    print(random.choice(DAILY_TASKS))


def main():
    clear_screen()
    print("Welcome to Daily Motivation!")
    print("-" * 40)

    show_quote()
    show_task()

    print("\nTake one small step at a time.")
    print("-" * 40)

    try:
        input("\nPress Enter to finish...")
    except (KeyboardInterrupt, EOFError):
        print("\nSession ended.")

    print("\nThank you for using Daily Motivation!")


if __name__ == "__main__":
    main()
  
