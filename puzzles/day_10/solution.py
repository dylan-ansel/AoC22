with open('input.txt', 'r') as f:
    INPUT = f.read()

INSTR = [line.split(' ') for line in INPUT.split('\n')]


class CPU:
    def __init__(self, relevant_cycles):
        self.cycle = 0
        self.x = 1
        self.relevant_cycles = relevant_cycles
        self.signal_strength = 0
        self.all_relevant_strengths = []

    @property
    def sum_of_relevant_strengths(self):
        return sum(self.all_relevant_strengths)

    def check_relevant_cycles(self):
        if self.cycle in self.relevant_cycles:
            self.signal_strength = self.x * self.cycle
            self.all_relevant_strengths.append(self.signal_strength)

    def add_to_cycle(self, value):
        for i in range(value):
            self.cycle += 1
            self.check_relevant_cycles()

    def execute_noop(self):
        self.add_to_cycle(1)

    def execute_addx(self, value):
        self.add_to_cycle(2)
        self.x += value


def p1():
    relevant = [20, 60, 100, 140, 180, 220]
    cpu = CPU(relevant)

    for line in INSTR:
        instruction = line[0]
        if instruction == 'noop':
            cpu.execute_noop()
        elif instruction == 'addx':
            amount = int(line[1])
            cpu.execute_addx(amount)
    return cpu.sum_of_relevant_strengths


def p2():
    pass


if __name__ == '__main__':
    print(f'p1: {p1()}, p2: {p2()}')
