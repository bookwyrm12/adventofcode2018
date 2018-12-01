#####################################
#  Advent of Code 2018              #
#  Day 1: Chronal Calibration       #
#  April Nickel                     #
#####################################

# Get the data
with open('day1.in') as f:
    data = f.read()


# Part 1
def part1(freq):
    freq = [int(x) for x in freq.splitlines()]
    freq = sum(freq)
    print('Part 1: Final Frequency: {}'.format(freq))


# Do the stuff
part1(data)
