'''
--- Day 1: Report Repair ---
After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island. Surely, Christmas will go on without you.

The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of a starfish; the locals just call them stars. None of the currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.

To save your vacation, you need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456
In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?

__
I could user itertools hear to just check every combination but my plan is a bit different:
I am going to sort the entier list into seperate lists based on the last digit (1,9) (2,8) ect. because the they must add up to 10 for the math to work. 
once I have my lists I will sort each of those and iterate through each half othe list checking for the math. 
i.e check the first item in my ones and nines list agaist all numbers that end in nine and then do the same with 
the next item in the list. 
once I find the match I can return it.


'''
file = 'adventofcode2020/day_1_report_repair_input.txt'
# innit lists to sort 
zeros = []
ones_nines = []
twos_eights = []
threes_seves = []
fours_sixes = []
fives = []
# read file into sorted lists 
with open(file) as f:
    for line in f:
        line = line.replace('\n','')
        if line[-1] == '0':
            zeros.append(line)
        elif line[-1]=='1' or line[-1]=='9':
            ones_nines.append(line)
        elif line[-1]=='2' or line[-1]=='8':
            twos_eights.append(line)
        elif line[-1]=='3' or line[-1]=='7':
            threes_seves.append(line)
        elif line[-1]=='4' or line[-1]=='6':
            fours_sixes.append(line)
        else:
            fives.append(line)



def finder(numbers:list)->int:
    #sort the list by last digit 
    numbers = sorted(numbers, key = lambda n: n[-1])
    i = 0 
    j = len(numbers)-1
    x = True
    # iterate through each half of the list checking for a match 
    while x:
        # if last digit at i and j are the same reset to check next seriese of numbers
         if numbers[i][-1] == numbers[j][-1]:
            i+=1
            j = len(numbers)-1
        #if we found a match return it 
         if int(numbers[i]) + int(numbers[j]) == 2020:
            return numbers[i],numbers[j], int(numbers[i]) * int(numbers[j])
         else:
            j-=1
        # if i and j are at same index we have checked all numbers and have nopt returned a match so return false. 
         if i==j:
            x = False
    return False

lists = [ones_nines,twos_eights,threes_seves,fours_sixes,fives]
# for each of the sorted lists check for match and return it when found. 
for l in lists:
    if finder(l):
        print(finder(l))
    
