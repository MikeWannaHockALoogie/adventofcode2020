'''
--- Day 3: Toboggan Trajectory ---
With the toboggan login problems resolved, you set off toward the airport. While travel by toboggan might be easy, it's certainly not safe: there's very minimal steering and the area is covered in trees. You'll need to see which angles will take you near the fewest trees.

Due to the local geology, trees in this area only grow on exact integer coordinates in a grid. You make a map (your puzzle input) of the open squares (.) and trees (#) you can see. For example:

..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
These aren't the only trees, though; due to something you read about once involving arboreal genetics and biome stability, the same pattern repeats to the right many times:

..##.........##.........##.........##.........##.........##.......  --->
#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........#.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...##....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
You start on the open square (.) in the top-left corner and need to reach the bottom (below the bottom-most row on your map).

The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers rational numbers); start by counting all the trees you would encounter for the slope right 3, down 1:

From your starting position at the top-left, check the position that is right 3 and down 1. Then, check the position that is right 3 and down 1 from there, and so on until you go past the bottom of the map.

The locations you'd check in the above example are marked here with O where there was an open square and X where there was a tree:

..##.........##.........##.........##.........##.........##.......  --->
#..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........X.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...#X....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
In this example, traversing the map using this slope would cause you to encounter 7 trees.

Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?

--- Part Two ---
Time to check the rest of the slopes - you need to minimize the probability of a sudden arboreal stop, after all.

Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:

Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together, these produce the answer 336.

What do you get if you multiply together the number of trees encountered on each of the listed slopes?

----
part one 
1.)read file into nested lists of 0,1
2.)  create list to store values
3.)traverse nested lists adding each step to the list 
4.) sum up stored values 
For part two 
5.) create list of tupples for slopes to check and iterate through that list with above logic for each slope 
'''
import math

def load_terrain(file)->list:
    '''
    loads a terrain file converting it to ones and zeros for eash counting returing a nested list 
    '''
    terrain = []
    with open(file) as f:
        count = 0 
        for line in f:
            x = []
            for i in line:
                if i =='.':
                    x.append(0)
                else:
                    x.append(1)
            terrain.append(x)
    return terrain


def check_path(slope:tuple, terrain:list)->int:
    '''
    given a terrain and a slope(x,y) iterates through the terrain to count number of trees encountered
    '''
    col =0 # set col to 0 as atarting point
    total = [] # init list to get total at the end 
    x,y = slope[0], slope[1] # get x and y values for slope 
    for row in range(0,len(terrain),y):
        # iterate through each row and column useing x,y from slope adding each step to the total list 
        total.append(terrain[row][col])
        width = len(terrain[row])
        col+=x
        if col >= width-1:
            col =col-(width-1)
    #return the total number trees encountered for this slope 
    return sum(total)
    
def check_all_paths(slopes:list,terrain:list)->list: 
    '''
    iterates through a list of solpes (x,y) and returns a list of trees encoutered for each slope 
    '''
    l = [] # init list for tracking trees counted on each slope
    for slope in slopes: # iterates through slopes and checks path for trees 
        l.append(check_path(slope,terrain))
    return l

def solve(file,slopes:list)->int:
    '''
    loads file, and checks each path for trees counted returning the answer for day three of AOC 
    '''
    terrain = load_terrain(file)
    tree_counts = check_all_paths(slopes,terrain)

    return math.prod(tree_counts)

file = 'day_3_toboggan_trajectorry_input.txt'

#part 1 
print(solve(file,[(3,1)]))
#part 2
slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
print(solve(file,slopes))
