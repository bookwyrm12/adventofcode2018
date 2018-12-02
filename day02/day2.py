########################################
#  Advent of Code 2018                 #
#  Day 2: Inventory Management System  #
#  April Nickel                        #
########################################

# Get the data
with open('day2.in') as f:
    data = f.read()


# Part 1
def part1(boxIds):
    count2 = count3 = 0
    boxIds = [x for x in boxIds.splitlines()]
    
    for i in boxIds:
        countLetter = {
            1: [],
            2: [],
            3: [],
            4: []
        }
        for letter in i:
            if letter in countLetter[1]:
                countLetter[1].remove(letter)
                countLetter[2].append(letter)
            elif letter in countLetter[2]:
                countLetter[2].remove(letter)
                countLetter[3].append(letter)
            elif letter in countLetter[3]:
                countLetter[3].remove(letter)
                countLetter[4].append(letter)
            elif letter not in countLetter[4]:
                countLetter[1].append(letter)
        if len(countLetter[2]) > 0:
            count2 += 1
        if len(countLetter[3]) > 0:
            count3 += 1
    
    checksum = count2 * count3
    print('Part 1: Checksum for list of box IDs: {}'.format(checksum))


# Do the stuff
part1(data)
