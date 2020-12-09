from itertools import combinations
file = 'day_9_encoding_error_input.txt'
data = [int(i) for i in open(file).readlines()]


def find_error(data: list, preamble_len: int):
    '''
    checks data t0 find any error. sum == to current number not found in previous 25 numbers  
    '''
    # start with preamble to check for sums
    current_nums = data[:preamble_len]
    # combination of all sums found in preamble
    sums = [sum(i) for i in combinations(current_nums, 2)]
    # data to check
    check_data = data[preamble_len:]
    # iterate through data that needs checking to find if one is not in sums
    for i in check_data:
        if i not in sums:
            return i
        else:
            # if number is valid update check_nums and sums for new values
            discard = current_nums.pop(0)
            current_nums.append(i)
            sums = [sum(i) for i in combinations(current_nums, 2)]


def part_two(data, checksum):
    '''
    iterates through increasingly smaller windows of data to find sequence of sontiguous nums that sum up to check sum 
    '''
    # sets index to start searc hthrough so that it can be reset in any iteration
    idx = data.index(checksum)-1
    # index taht will be altered for each iteration
    temp_idx = data.index(checksum)-1
    # index to start at for each iteration
    i = 0
    while sum(data[i:temp_idx]) != checksum:
        # when sum of slice = check sum exit loop and return answer
        if sum(data[i:temp_idx]) < checksum:
            # if we start end up with a sum that is less than check sum increase starting index by 1 and rest upper index
            i += 1
            temp_idx = idx
        temp_idx -= 1
        # reduce end index until we find a match
        if i == temp_idx:
            # if start index and temp index are same, and we have not found a match and sum is > check sum there is not match.
            return 'no valid num'
    return max(data[i:temp_idx]) + min(data[i:temp_idx])


print(find_error(data, 25))
print(part_two(data, find_error(data, 25)))
