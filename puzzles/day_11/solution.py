import operator
import numpy as np

with open('input.txt', 'r') as f:
    INPUT = f.read()

INSTR = [line for line in INPUT.split('\n')]
OPERATORS = {"+": operator.add, "*": operator.mul}


class Item:
    def __init__(self, monkey, worry_level):
        self.monkey = monkey
        self.worry = worry_level

    def reduce_worry(self):
        self.worry = self.worry // 3


class Monkey:
    def __init__(self, ordinal):
        self.ordinal = ordinal
        self.divisor = 0
        self.recipient_if_true = None
        self.recipient_if_false = None
        self.operator = None
        self.operand = 0
        self.is_using_old_worry_as_operand = False
        self.owned_items = []
        self.inspect_count = 0

    def turn(self, manage_worry):
        self.get_list_of_owned_items()
        for item in self.owned_items:
            self.inspect_count += 1
            self.operation(item)
            if manage_worry: item.reduce_worry()
            self.throw(self.test(item), item)

    def get_list_of_owned_items(self):
        self.owned_items = []
        for item in ITEMS:
            if item.monkey == self:
                self.owned_items.append(item)

    def operation(self, item):
        if self.is_using_old_worry_as_operand:
            item.worry = self.operator(item.worry, item.worry)
        else:
            item.worry = self.operator(item.worry, self.operand)

    def test(self, item):
        if item.worry % self.divisor == 0:
            return True
        else:
            return False

    def throw(self, passed, item):
        if passed:
            item.monkey = self.recipient_if_true
        else:
            item.monkey = self.recipient_if_false
        ITEMS.remove(item)            # ensures the order of item evaluation is kosher
        ITEMS.append(item)


def create_monkeys():
    monkeys = []
    for i, instruction in enumerate(INSTR):
        if i % 7 == 0:
            monkeys.append(Monkey(i // 7))

    return monkeys


def create_items():
    items = []
    for i, instruction in enumerate(INSTR):
        if i % 7 == 1:
            for item in instruction.split(': ')[1].split(', '):
                monkey = MONKEYS[(i - 1) // 7]              # assign monkey object
                items.append(Item(monkey, int(item)))       # pass monkey object as 'parent'

    return items


def assign_operations_and_tests():
    # assign operation
    for i, instruction in enumerate(INSTR):
        offset = 2
        if i % 7 == offset:
            # define operator
            monkey = MONKEYS[(i - offset) // 7]
            monkey.operator = OPERATORS[instruction.split('= old ')[1][0]]
            # define operand
            operand = instruction.split('= old ')[1][2:]
            if operand == "old":
                monkey.is_using_old_worry_as_operand = True
            else:
                monkey.operand = int(operand)

    # assign test
    for i, instruction in enumerate(INSTR):
        offset = 3
        if i % 7 == offset:
            monkey = MONKEYS[(i - offset) // 7]
            monkey.divisor = int(instruction.split('by ')[1])

    # assign recipient for True condition
    for i, instruction in enumerate(INSTR):
        offset = 4
        if i % 7 == offset:
            monkey = MONKEYS[(i - offset) // 7]
            recipient = MONKEYS[int(instruction.split('monkey ')[1])]
            monkey.recipient_if_true = recipient

    # assign recipient for False condition
    for i, instruction in enumerate(INSTR):
        offset = 5
        if i % 7 == offset:
            monkey = MONKEYS[(i - offset) // 7]
            recipient = MONKEYS[int(instruction.split('monkey ')[1])]
            monkey.recipient_if_false = recipient


def p1():
    rounds = 20
    manage_worry = True

    for _ in range(rounds):
        for monkey in MONKEYS:
            monkey.turn(manage_worry)

    inspections = []
    for monkey in MONKEYS:
        inspections.append(monkey.inspect_count)
    inspections.sort(reverse=True)
    product = np.prod(inspections[0:2])

    return product


def p2():
    # I
    # GIVE
    # UP
    pass
    # YOU
    # WIN


if __name__ == '__main__':
    MONKEYS = create_monkeys()
    ITEMS = create_items()
    assign_operations_and_tests()
    print(f'p1: {p1()}, p2: {p2()}')
