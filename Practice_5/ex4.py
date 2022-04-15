import random
from collections import defaultdict
import inspect
from time import time
from ast import *


class Locator(NodeVisitor):
    def __init__(self):
        self.locs = defaultdict(list)

    def visit(self, node):
        self.locs[type(node)].append(node)
        self.generic_visit(node)


class Mutator(NodeTransformer):
    bin_operators = {
        Add: [Sub, Mult, Div, FloorDiv, Mod, LShift, RShift, BitOr, BitAnd, Pow],
        Sub: [Add, Mult, Div, FloorDiv, Mod, LShift, RShift, BitOr, BitAnd, Pow],
        Mult: [Sub, Add, Div, FloorDiv, Mod, LShift, RShift, BitOr, BitAnd, Pow],
        Div: [Sub, Mult, Add, FloorDiv, Mod, LShift, RShift, BitOr, BitAnd, Pow],
        FloorDiv: [Sub, Mult, Div, Add, Mod, LShift, RShift, BitOr, BitAnd, Pow],
        Mod: [Sub, Mult, Div, FloorDiv, Add, LShift, RShift, BitOr, BitAnd, Pow],
        LShift: [Sub, Mult, Div, FloorDiv, Mod, Add, RShift, BitOr, BitAnd, Pow],
        RShift: [Sub, Mult, Div, FloorDiv, Mod, LShift, Add, BitOr, BitAnd, Pow],
        BitOr: [Sub, Mult, Div, FloorDiv, Mod, LShift, RShift, Add, BitAnd, Pow],
        BitAnd: [Sub, Mult, Div, FloorDiv, Mod, LShift, RShift, BitOr, Add, Pow],
        Pow: [Sub, Mult, Div, FloorDiv, Mod, LShift, RShift, BitOr, BitAnd, Add]
    }

    bool_operators = {
        And: Or,
        Or: And
    }

    compare_operators = {
        Eq: [NotEq, Lt, LtE, Gt, GtE],
        NotEq: [Eq, Lt, LtE, Gt, GtE],
        Lt: [NotEq, Eq, LtE, Gt, GtE],
        LtE: [NotEq, Lt, Eq, Gt, GtE],
        Gt: [NotEq, Lt, LtE, Eq, GtE],
        GtE: [NotEq, Lt, LtE, Gt, Eq],
        Is: [NotEq, Lt, LtE, Gt, GtE, Eq, IsNot],
        IsNot: [NotEq, Lt, LtE, Gt, GtE, Is, Eq],
        In: [NotEq, Lt, LtE, Gt, GtE, Eq, NotIn],
        NotIn: [NotEq, Lt, LtE, Gt, GtE, In, Eq]
    }

    def visit_BinOp(self, node):
        if type(node.op) in self.bin_operators.keys():
            new_op = random.choice(self.bin_operators[type(node.op)])
            new_node = BinOp(
                left=node.left,
                op=new_op(),
                right=node.right
            )
            copy_location(new_node, node)
            fix_missing_locations(new_node)
            return new_node
        return node

    def visit_BoolOp(self, node):
        if type(node.op) in self.bool_operators.keys():
            new_op = random.choice(self.bool_operators[type(node.op)])
            new_node = BoolOp(
                values=node.values,
                op=new_op()
            )
            copy_location(new_node, node)
            fix_missing_locations(new_node)
            return new_node
        return node

    def visit_Compare(self, node):
        op_ind = random.choice(range(len(node.ops)))
        op = node.ops[op_ind]
        if type(op) in self.compare_operators.keys():
            new_ops = node.ops
            new_op = random.choice(self.compare_operators[type(op)])
            new_ops[op_ind] = new_op()
            new_node = Compare(
                left=node.left,
                ops=new_ops,
                comparators=node.comparators
            )
            copy_location(new_node, node)
            fix_missing_locations(new_node)
            return new_node
        return node

    def visit_Constant(self, node):
        if isinstance(node.value, int):
            new_node = Constant(
                value=node.value + random.choice([-1, 1])
            )
            copy_location(new_node, node)
            fix_missing_locations(new_node)
            return new_node
        return node
    # random construct for key in dict
    def __init__(self, locs):
        random.seed(time())
        mutant_types = {BinOp, BoolOp, Compare, Constant}
        node_type = None
        while node_type not in mutant_types:
            node_type = random.choice(list(locs.keys()))
        self.target = random.choice(locs[node_type])

    def visit(self, node):
        if self.target != node:
            return self.generic_visit(node)
        return super(Mutator, self).visit(self.target)

# func number of changes
def mutate_code(src, max_changes):
    tree = parse(src)
    loc = Locator()
    loc.visit(tree)
    mut = Mutator(loc.locs)
    for _ in range(random.randint(1, max_changes)):
        mut.visit(tree)
    return unparse(tree)


def make_mutants(func, size, max_changes):
    mutant = src = unparse(parse(inspect.getsource(func)))
    mutants = [src]
    time_start = time()
    while len(mutants) < size + 1:
        time_end = time()
        while mutant in mutants:
            mutant = mutate_code(src, max_changes)
            time_end = time()
            if time_end - time_start > 2:
                break
        if time_end - time_start > 2:
            break
        mutants.append(mutant)
    return mutants[1:]


def mut_test(func, test, size=20, max_changes=1):
    survived = []
    mutants = make_mutants(func, size, max_changes)
    print('Mutants:')
    print('Amount of mutants: {}'.format(len(mutants)))
    print(*mutants, sep='\n')
    for mutant in mutants:
        try:
            exec(mutant, globals())
            test()
            survived.append(mutant)
        except:
            pass
    print('\nSurvived:')
    print('Amount of survived: {}'.format(len(survived)))
    print(*survived, sep='\n')


# Умножение на два
def foo(n):
    return n * 2


def test():
    func = globals()['foo']
    assert func(2) == 4


# Фибоначчи
# def foo(n):
#     if n in (1, 2):
#         return 1
#     return foo(n - 1) + foo(n - 2)
#
#
# def test():
#     func = globals()['foo']
#     assert func(6) == 8
#     assert func(5) == 5
#     assert func(10) == 55
#     assert func(1) == 1
#     assert func(2) == 1
#



mut_test(foo, test, 100)
