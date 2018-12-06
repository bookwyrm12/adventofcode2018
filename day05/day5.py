#################################
#  Advent of Code 2018          #
#  Day 5: Alchemical Reduction  #
#  April Nickel                 #
#################################


# Get the data
with open('day5.in') as f:
    data = f.read()


# Part 1
def part1(polymer):
    polymer = polymer.strip()
    polymer_new = react(polymer)

    answer = len(polymer_new)
    print('Part 1: # Remaining Units: {}'.format(answer))


# Helper
def react(polymer):
    polymer_new = []

    for i in range(len(polymer)):
        polymer_new.append(polymer[i])
        if len(polymer_new) > 1:
            # 32 is the distance between the upper- & lower-case ord of the same char
            if abs(ord(polymer_new[-1]) - ord(polymer_new[-2])) == 32:
                polymer_new.pop()
                polymer_new.pop()

    return polymer_new

# Do the stuff
part1(data)
