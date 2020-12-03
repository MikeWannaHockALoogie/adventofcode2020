'''
--- Day 2: Password Philosophy ---
Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we can't log in!" You ask if you can take a look.

Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?
----

1.) create dict() with desired column headers as keys (lower bound, upper bound, letter, password)
2.) pre-process data and load into dict with boolean values for logic required for part 1 and 2
3.) load dict into pandas Df to simulate database. 
4.) select data for part one and two to get counts 

'''
import pandas as pd 


file = 'adventofcode2020/day_2_password_philosophy_input.txt'

data = {'lower':[],'upper':[],'letter':[],'password':[],'count_correct':[],'true_false':[]}
with open(file) as f:
    for line in f:
        # clean data and split into dict for pandas 
        line = line.strip()
        #strip new line and whitspace
        line = line.replace('-',',')
        # replace  :, whitespace(1)  with a comma
        line = line.replace(':',',')
        line = line.replace(' ',',',1)
        # delete any remaining white space
        line = line.replace(' ', '')
        # split line into list
        line = line.split(',')
        # assign values to dict 
        data['lower'].append(line[0])
        data['upper'].append(line[1])
        data['letter'].append(line[2])
        data['password'].append(line[3])
        # column for part one answer count number of occurances of letter to for part cone
        data['count_correct'].append(int(line[0])<=line[3].count(line[2])<=int(line[1]))
        # column for part two anwer 
        data['true_false'].append(
            (
                line[3][int(line[0])-1]==line[2]
            and
            line[3][int(line[1])-1]!=line[2]
        ) or (
            line[3][int(line[0])-1]!=line[2]
            and
            line[3][int(line[1])-1]==line[2]
        )
        )
            

df = pd.DataFrame.from_dict(data)

x = df[df.count_correct ==True]
y = df[df.true_false == True]
print(x.shape[0])
print(y.shape[0])
