
file = 'day_5_binary_boarding_input.txt'
data = [line.strip('\n') for line in open(file).readlines()]
    
def to_binary(number:str)->str:
    '''
    takes boarding pass code and converts to binary number in string format 
    '''
    number= number.replace('F','0')
    number= number.replace('B','1')
    number= number.replace('R','1')
    number= number.replace('L','0')
    return number

def binary_converter(number:str)->int:
    '''
    takes binary number in string format and converts to decimal as an integer
    '''
    count = 0
    total = 0
    for i in range(len(number)-1,-1,-1):
        total += (int(number[i]) * (2 ** count))
        count +=1
    return total

def get_seat_id(number:str)->int:
    '''
    takes binary number in string format and gets seat ID 
    '''
    row = binary_converter(number[:7])
    column = binary_converter(number[-3:])
    seat_id = row * 8 + column
    return seat_id

def solver(number:str)->int:
    '''
    takes a boarding pass code converts it to binary and then gets a seat id 
    '''
    n = to_binary(number)
    return get_seat_id(n)

test = 'BFFFBBFRRR'
assert to_binary('FFF') == '000'
assert to_binary('BBB') == '111'
assert to_binary('RRR') == '111'
assert to_binary('LLL') == '000'
assert to_binary('FBRL') == '0110'
assert binary_converter('0')== 0
assert binary_converter('1')== 1
assert binary_converter('111')==7
assert binary_converter('1000110') ==70
assert to_binary(test) == '1000110111'
assert solver(test) == 567


def find_my_seat(data:list)->int:
    '''
    iterates though the list of boarding passes to find the gap in and returns the missing boarding pass. 
    '''
    seat_ids = sorted([solver(line) for line in data ])
    for i in range(0,len(seat_ids)-1):
        if seat_ids[i+1]-seat_ids[i] > 1:
            return int(seat_ids[i])+1

print(max([solver(line) for line in data]))
print(find_my_seat(data))