'''
for day 7 psuedo
1.)import instructions into pandas data frame
2.)follow imported instructions until one is repeated using the 'executed column' to keep track of lines already ran
3.)return accumulator
--- part two
4.) repeat part one but any time a 'jmp' or 'nop' command is encountered create a copy of original df with that specific comand switched
5.) add new_df to list
6.) when instruction is repeated return list instead of accumulator
7.) iterate over list using code from part one and return accumulator if we move past final command

'''
import pandas as pd
from copy import deepcopy
file = [line.strip().split(' ') for line in open(
    'day_8_handheld_halting_input.txt').readlines()]
data = {'cmd': [], 'amt': [], 'executed': []}
for line in file:
    data['cmd'].append(line[0])
    data['amt'].append(line[1])
    data['executed'] = False


df = pd.DataFrame.from_dict(data)
print(df.shape)
# print(df.head())


class Instruction():
    def __init__(self, id, cmd, amt, executed=False, link=None):
        self.id = id
        self.cmd = cmd
        self.amt = amt
        self.executed = executed
        self.link = link
        self.valid_commands = ['jmp', 'acc', 'nop']

    '''def __str__(self):
        return f" id: {self.id}, cdm: {self.cmd}, amt: {self.amt}, executed: {self.executed}, link: {self.link}"'''

    def is_valid(self) -> bool:
        return self.cmd in self.valid_comands

    def is_executed(self) -> bool:
        return self.executed

    def get_command(self) -> str:
        return self.cmd

    def get_amount(self) -> int:
        return int(self.amt)

    def get_link(self):
        return self.link

    def get_id(self):
        return self.id

    def set_command(self, new_command) -> None:
        if new_command in self.valid_commands:
            self.cmd = new_command

    def set_amount(self, new_amount: int) -> None:
        self.amount = new_amount

    def set_link(self, instruction) -> None:
        self.link = instruction

    def execute(self) -> None:
        self.executed = True


class InstructionList():
    def __init__(self, instructions: dict, accumulator=0, start_id=0):
        self.instructions = instructions
        self.current_inst = self.instructions[start_id]
        self.accumulator = accumulator

    def __repr__(self):
        return self.accumulator

    def compile(self):
        for idx, inst in self.instructions.items():
            if inst.get_command() == 'jmp':
                amt = inst.get_amount()
            else:
                amt = 1
            if idx + 1 in self.instructions.keys():
                inst.set_link(instructions[idx + amt])
            else:
                inst.set_link(None)
            # print(inst.executed)

    def get_current_inst(self):
        return self.current_inst

    def set_current_inst(self, next):
        self.get_current_inst = next

    def get_accumulator(self):
        return self.accumulator

    def set_accumulator(self, amt):
        self.accumulator += amt

    def execute(self):
        instruction = self.current_inst

        if instruction.get_command() == 'acc':
            self.set_accumulator(instruction.get_amount())

        instruction.execute()

    def is_loop(self):
        i = self.get_current_inst()

        seen = []
        while i.id not in seen:
            ident = i.id
            if i.get_link() == None:
                return False
            i = i.get_link()
            seen.append(ident)

        return True

    def run(self):
        while True:
            if self.current_inst.id > len(self.instructions.keys())-1:
                return self.get_accumulator()
            self.execute()
            next = self.current_inst.get_link()
            if next == None:
                return self.get_accumulator()
            if next.is_executed():
                return self.get_accumulator()
            self.current_inst = next

    def fix(self):
        count = 0
        i = self.get_current_inst()

        while True:
            # print(i.id, i.cmd, i.amt)
            if i.id > len(self.instructions):
                break
            if i.get_command() == 'jmp':
                count += 1
                new_program = InstructionList(
                    deepcopy(self.instructions), start_id=i.id, accumulator=self.accumulator)
                new_program.instructions[i.id].set_command('nop')
                new_program.compile()
                if not new_program.is_loop():
                    return new_program.run()
            elif i.get_command() == 'nop':
                count += 1
                new_program = InstructionList(
                    deepcopy(self.instructions), start_id=i.id, accumulator=self.accumulator)
                new_program.instructions[i.id].set_command('jmp')
                # print(new_program.instructions[i.id].get_command())
                new_program.compile()
                if not new_program.is_loop():
                    return new_program.run()
            self.execute()
            i = i.get_link()
            self.current_inst = i
            if i.is_executed():
                print('link is executed')
                print(count)
                break


instructions = dict()
for i in range(len(file)):
    instruction = Instruction(id=i, cmd=file[i][0], amt=file[i][1])
    instructions[i] = instruction

static_code = InstructionList(instructions)
static_code.compile()
program = deepcopy(static_code)
print(program.run())
program = deepcopy(static_code)
print('is loop', program.is_loop())
program = deepcopy(static_code)
print(program.fix())
print(program.run())
print(program.fix())


def run(df1, i=0):
    df = df1.copy(deep=True)
    accumulator = 0

    df_list = []
    while True:
        if i > df.shape[0]-1:
            # part two solution condition
            return accumulator
        if df.loc[i, 'executed'] == True:
            # part two return all list of all possible changes to df where exactly one 'nop' <-> 'jmp.
            return df_list
            # part one solution comented out
            # return accumulator
        if df.loc[i, 'cmd'] == 'jmp':
            df.loc[i, 'executed'] = True
            new_df = df1.copy(deep=True)
            new_df.loc[i, 'cmd'] = 'nop'
            df_list.append(new_df)
            i += int(df.loc[i, 'amt'])
        elif df.loc[i, 'cmd'] == 'acc':
            accumulator += int(df.loc[i, 'amt'])
            df.loc[i, 'executed'] = True
            i += 1
        elif df.loc[i, 'cmd'] == 'nop':
            df.loc[i, 'executed'] = True
            new_df = df1.copy(deep=True)
            new_df.loc[i, 'cmd'] = 'jmp'
            df_list.append(new_df)
            i += 1
        else:
            print(i)
            print(f'unrecognized command \n {df.loc[i:"cmd"]}', i)
            break


def part_two(df_list):
    for d in df_list:
        a = run(d)
        if type(a) == int:
            return a
    return None


'''df_list = run(df)
print(part_two(df_list))'''
