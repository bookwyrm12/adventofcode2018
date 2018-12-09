#######################################
#  Advent of Code 2018                #
#  Day 3: No Matter How You Slice It  #
#  April Nickel                       #
#######################################

# Imports
import re


# Get the data
with open('day3.in') as f:
    data = f.read()


# Part 1
def part1(claims):
    claims = claims.splitlines()

    fabric = {}
    overlap = 0
    for c in claims:
        id, coords, w, h = get_claim(c)
        for x in range(int(coords['x']), int(coords['x']) + int(w)):
            for y in range(int(coords['y']), int(coords['y']) + int(h)):
                if (x,y) in fabric:
                    if id not in fabric[(x,y)]:
                        fabric[(x,y)].append(id)
                else:
                    fabric[(x,y)] = [id]

    overlap = len([ fabric[x] for x in fabric if len(fabric[x]) > 1 ])

    print('Part 1: Square inches of fabric in 2+ claims: {}'.format(overlap))


# Helper
def get_claim(claim):
    reg = re.search('#([0-9]+)', claim)
    id = reg.group(1)
    reg = re.search('@ ([0-9]+),([0-9]+)', claim)
    coords = { 'x': reg.group(1), 'y': reg.group(2) }
    reg = re.search(': ([0-9]+)x([0-9]+)', claim)
    w = reg.group(1)
    h = reg.group(2)
    return id, coords, w, h


# Do the stuff
part1(data)
