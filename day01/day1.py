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


# Part 2
def part2(freqs):
    freqs = [int(x) for x in freqs.splitlines()]
    freq_dup = find_dup_freq(freqs, 0)
    print('Part 2: Frequency Reached Twice: {}'.format(freq_dup))


# Part 2 Helper
def find_dup_freq(freqs, freq_cur):
    freq_res = {}
    while True:
        for i in freqs:
            freq_cur += i
            if freq_cur in freq_res:
                return freq_cur
            else:
                freq_res[freq_cur] = True


# Do the stuff
part1(data)
part2(data)
