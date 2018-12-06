##############################
#  Advent of Code 2018       #
#  Day 4: Repose Record      #
#  April Nickel              #
##############################

# Imports
import re


# Get the data
with open('day4.in') as f:
    data = f.read()


# Part 1
def part1(records):
    records = sorted(records.splitlines())
    
    guard_data = {}
    guard_cur = None
    rec_mins = falls_asleep = wakes_up = 0
    
    for rec in records:
        if "begins shift" in rec:
            guard_cur = re.search('Guard #([0-9]+)', rec).group(1)
            if guard_cur not in guard_data:
                guard_data[guard_cur] = {
                    'asleep_min_tally': {},
                    'asleep_total': 0,
                    'most_asleep_min': None
                }
            
        elif "falls asleep" in rec:
            falls_asleep = re.search('00:([0-9][0-9])\]', rec).group(1)
            
        elif "wakes up" in rec:
            wakes_up = re.search('00:([0-9][0-9])\]', rec).group(1)
            rec_mins = int(wakes_up) - int(falls_asleep)
            guard_data[guard_cur]['asleep_total'] += rec_mins
            for i in range(int(falls_asleep), int(wakes_up)):
                if i not in guard_data[guard_cur]['asleep_min_tally']:
                    guard_data[guard_cur]['asleep_min_tally'][i] = 0
                guard_data[guard_cur]['asleep_min_tally'][i] += 1
                if not guard_data[guard_cur]['most_asleep_min']:
                    guard_data[guard_cur]['most_asleep_min'] = i
                elif guard_data[guard_cur]['asleep_min_tally'][i] > guard_data[guard_cur]['asleep_min_tally'][guard_data[guard_cur]['most_asleep_min']]:
                    guard_data[guard_cur]['most_asleep_min'] = i
    
    guard = minute = 0
    guard = max([(int(guard_data[x]['asleep_total']), x) for x in guard_data])[1]
    minute = guard_data[guard]['most_asleep_min']
    answer = int(guard) * int(minute)
    print('Part 1: Guard ID * Minute: {}'.format(answer))


# Do the stuff
part1(data)
