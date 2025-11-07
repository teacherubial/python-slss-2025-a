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

    # buckets to hold all votes
    blenz = 0
    bubble_queen = 0
    sun_tea = 0
    heytea = 0
    coco = 0
    fresh_t = 0

    # Show all the choices
    print("Vote for your favourite from the list. ")
    print("Give the letter of your choice.")
    for choice in CHOICES:
        print(choice)

    # Ask the user for their choice
    vote = input("Your vote: ").strip(",.?! ").lower()
    # Keep track of a tally
    if vote == "a":
        blenz = blenz + 1
    elif vote == "b":
        bubble_queen += 1
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
