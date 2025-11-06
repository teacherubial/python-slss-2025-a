# Numbers and Operations
# Author: Ubial
# 5 November 2025

# Work with numbers and operations

# Create an algorithm to gather
# data to find the most popular
# bubble tea place around us

# Version 1
def vote_listed_choices():
    """Display all choices
    5 users vote for their choice
    Results will be printed"""
    CHOICES = [
        "A. Blenz",
        "B. Bubble Queen",
        "C. Sun Tea",
        "D. heytea",
        "E. CoCo",
        "F. Fresh T"
    ]

    # Show all the choices
    print("Vote for your favourite from the list. ")
    print("Give the letter of your choice.")
    for choice in CHOICES:
        print(choice)

    # Ask the user for their choice
    # Keep track of a tally
    # Data analysis
    # Give the raw scores
    # Give scores as a percentage

# Version 2
# Ask the user to give their
# favourite bubble tea place
# Keep track of a tally
# Data analysis
# Give the raw scores
# Give scores as a percentage

def main():
    vote_listed_choices()

if __name__ == "__main__":
    main()
