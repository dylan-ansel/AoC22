with open('input.txt', 'r') as f:
    INPUT = f.read()

INSTR = [line.split(' ') for line in INPUT.split('\n')]


class CPU:
    def __init__(self, width, relevant_cycles=[]):
        self.width = width
        self.cycle = 0
        self.x = 1
        self.relevant_cycles = relevant_cycles
        self.signal_strength = 0
        self.all_relevant_strengths = []
        self.screen = ""

    @property
    def sum_of_relevant_strengths(self):
        return sum(self.all_relevant_strengths)

    @property
    def sprite(self):
        return range(self.x - 1, self.x + 2)   # i might consider putting the modulo here for readability

    def check_relevant_cycles(self):
        if self.cycle in self.relevant_cycles:
            self.signal_strength = self.x * self.cycle
            self.all_relevant_strengths.append(self.signal_strength)

    def draw_screen(self):
        if self.cycle % self.width in self.sprite:
            self.screen += "#"
        else:
            self.screen += "."
        if self.cycle % self.width == self.width - 1:
            self.screen += "\n"

    def print_screen(self):
        print(self.screen)

    def add_to_cycle(self, value):
        for i in range(value):
            self.draw_screen()
            self.cycle += 1
            self.check_relevant_cycles()

    def execute_noop(self):
        self.add_to_cycle(1)

    def execute_addx(self, value):
        self.add_to_cycle(2)
        self.x += value


def create_cpu(width, relevant_cycles=[]):
    cpu = CPU(width, relevant_cycles)

    for line in INSTR:
        instruction = line[0]
        if instruction == 'noop':
            cpu.execute_noop()
        elif instruction == 'addx':
            amount = int(line[1])
            cpu.execute_addx(amount)

    return cpu


def p1():
    relevant_cycles = [20, 60, 100, 140, 180, 220]
    cpu = create_cpu(40, relevant_cycles)
    return cpu.sum_of_relevant_strengths


def p2():
    cpu = create_cpu(40)
    return cpu.screen


if __name__ == '__main__':
    print(f'p1: {p1()}, p2: \n\n{p2()}')
