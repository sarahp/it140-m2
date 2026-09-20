"""
This program prompts the user for their name and age, calculates their
approximate birth year based on the current year, and then outputs a
personalized message with their name and birth year.
"""

# ==== Import Statements ====
from datetime import date

# ==== Constants ====
# Get current year from system as integer
CURRENT_YEAR = date.today().year

# ==== Main Function ====
def main() -> None:
    """Run the name-age program."""

    # Get user input.
    name = input("What is your name? ")
    age = int(input("How old are you? "))

    # Calculate user's approximate birth year.
    birth_year = CURRENT_YEAR - age

    # Output personalized message with the user's name and birth year.
    print(f"Hello {name}! You were born in {birth_year}.")


# ==== Main Guard ====
if __name__ == "__main__":
    main()
