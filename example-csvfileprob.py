# CSV File Problem
# Author: Ubial
# 20 November

def main():
    with open("data/sfu_best_cmpt120.csv") as f:
        # get rid of header
        _ = f.readline()

        # Vote buckets
        nature = 0
        chopped = 0
        subway = 0
        veggie = 0
        poke = 0

        for line in f:
            print(line)
            # get vote
            info = line.split(",")
            fave_healthy = info[-1].lower().strip()

            # add vote to bucket
            if fave_healthy == "nature's garden":
                nature += 1
            elif fave_healthy == "chopped leaf":
                chopped += 1

        # Results
        print("----------------------")
        print("Results: ")
        print(f"Nature's Garden: {nature}")
        print(f"Chopped Leaf: {chopped}")
        print(f"Subway: {subway}")
        print(f"Veggie Lunch: {veggie}")
        print(f"Steve's Poke Bar: {poke}")
        print("----------------------")


if __name__ == "__main__":
    main()
