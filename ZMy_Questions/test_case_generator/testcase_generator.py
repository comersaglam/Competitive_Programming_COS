from util import randint, randints

#N, S1, S2, H, T, C = list(map(int, input().split()))

import random
from typing import List, Tuple, Union

from tqdm import tqdm

from generator_util import gen_tree, randint, randints

class Input:
    n: int
    s1: int
    s2: int
    edges1: List[Tuple[int, int, int]] # u, v, w
    edges2: List[Tuple[int, int, int]] # u, v, w
    h : int
    t : int
    c : int

    def __init__(self, n: int, s1: int, s2: int, edges1: List[Tuple[int, int, int]], edges2: List[Tuple[int, int, int]],h: int, t: int, c: int) -> None:
        self.n = n  # number of nodes
        self.s1 = s1 # number of nodes in first set
        self.s2 = s2 # number of nodes in second set
        self.edges1 = edges1 # edges in first set
        self.edges2 = edges2 # edges in second set
        self.h = h # start node
        self.t = t # end node
        self.c = c # cost constant



MultipleTestInput = List[Input]


class Bounds:
    lower: int
    upper: int

    def __init__(self, lower: int, upper: int) -> None:
        self.lower = lower
        self.upper = upper

class Constraints:
    n: Bounds
    S1: Bounds
    S2: Bounds
    H: Bounds
    T: Bounds
    C: Bounds

    def __init__(self, n_bounds: Tuple[int, int], s1_bounds: Tuple[int, int], s2_bounds: Tuple[int, int], h_bounds: Tuple[int, int], t_bounds: Tuple[int, int], c_bounds: Tuple[int, int]) -> None:
        self.n = Bounds(*n_bounds)
        self.S1 = Bounds(*s1_bounds)
        self.S2 = Bounds(*s2_bounds)
        self.H = Bounds(*h_bounds)
        self.T = Bounds(*t_bounds)
        self.C = Bounds(*c_bounds)

    def validate(self, input: Union[Input, MultipleTestInput]) -> None:
        def validate_single(input: Input) -> None:
            assert self.n.lower <= input.n <= self.n.upper
            assert self.S1.lower <= input.s1 <= self.S1.upper
            assert self.S2.lower <= input.s2 <= self.S2.upper
            assert self.H.lower <= input.h <= self.H.upper
            assert self.T.lower <= input.t <= self.T.upper
            assert self.C.lower <= input.c <= self.C.upper

        if type(input) == Input:
            validate_single(input)
        elif type(input) == MultipleTestInput:
            for input in input:
                validate_single(input)


class InputGenerator:
    generalConstraints = Constraints(n_bounds=(1, 2 * 10**5), s1_bounds=(1, 2 * 10**5), s2_bounds=(1, 2 * 10**5), h_bounds=(1, 2 * 10**5), t_bounds=(1, 2 * 10**5), c_bounds=(1, 2 * 10**5))
    ### IMPLEMENT GENERATORS BEGIN ###

    def random_small(self, n_bounds: Tuple[int, int], s1_bounds: Tuple[int, int], s2_bounds: Tuple[int, int], h_bounds: Tuple[int, int], t_bounds: Tuple[int, int], c_bounds: Tuple[int, int]) -> Input:
        constraints = Constraints(n_bounds, s1_bounds, s2_bounds, h_bounds, t_bounds, c_bounds)
        n = randint(constraints.n.lower, constraints.n.upper)
        s1 = randint(constraints.S1.lower, constraints.S1.upper)
        s2 = randint(constraints.S2.lower, constraints.S2.upper)
        h = randint(constraints.H.lower, n)
        t = randint(constraints.T.lower, n)
        c = randint(constraints.C.lower, constraints.C.upper)
        edges1 = [(randint(1, n), randint(1, n), randint(1, 10)) for _ in range(s1)]
        edges2 = [(randint(1, n), randint(1, n), randint(1, 10)) for _ in range(s2)]
        input = Input(n, s1, s2, edges1, edges2, h, t, c)
        return self.validateAndReturn(input, constraints)
    
    def random(self, n_bounds: Tuple[int, int], s1_bounds: Tuple[int, int], s2_bounds: Tuple[int, int], h_bounds: Tuple[int, int], t_bounds: Tuple[int, int], c_bounds: Tuple[int, int]) -> Input:
        constraints = Constraints(n_bounds, s1_bounds, s2_bounds, h_bounds, t_bounds, c_bounds)
        n = randint(constraints.n.lower, constraints.n.upper)
        s1 = randint(constraints.S1.lower, constraints.S1.upper)
        s2 = randint(constraints.S2.lower, constraints.S2.upper)
        h = randint(constraints.H.lower, n)
        t = randint(constraints.T.lower, n)
        c = randint(constraints.C.lower, constraints.C.upper)
        edges1 = [(randint(1, n), randint(1, n), randint(1, 10**9)) for _ in range(s1)]
        edges2 = [(randint(1, n), randint(1, n), randint(1, 10**9)) for _ in range(s2)]
        input = Input(n, s1, s2, edges1, edges2, h, t, c)
        return self.validateAndReturn(input, constraints)

    def connected_random(self, n_bounds: Tuple[int, int], s1_bounds: Tuple[int, int], s2_bounds: Tuple[int, int], h_bounds: Tuple[int, int], t_bounds: Tuple[int, int], c_bounds: Tuple[int, int]) -> Input:
        constraints = Constraints(n_bounds, s1_bounds, s2_bounds, h_bounds, t_bounds, c_bounds)
        n = randint(constraints.n.lower, constraints.n.upper)
        h = randint(constraints.H.lower, n)
        t = randint(constraints.T.lower, n)
        c = randint(constraints.C.lower, constraints.C.upper)
        s1 = randint(max(constraints.S1.lower, n - 1), constraints.S1.upper)
        s2 = randint(max(constraints.S2.lower, n - 1), constraints.S2.upper)
        edges1 = gen_tree(s1)
        edges2 = gen_tree(s2)
        edges1 += [(randint(1, n), randint(1, n), randint(1, 10**9)) for _ in range(s1 - (n - 1))]
        edges2 += [(randint(1, n), randint(1, n), randint(1, 10**9)) for _ in range(s2 - (n - 1))]
        random.shuffle(edges1)
        random.shuffle(edges2)
        input = Input(n, s1, s2, edges1, edges2, h, t, c)
        return self.validateAndReturn(input, constraints)

    def max_chain(self) -> Input:
        constraints = self.generalConstraints
        n = constraints.n.upper
        m = n - 1
        nodes = list(range(2, n + 1))
        random.shuffle(nodes)
        nodes = [1] + nodes
        edges = []
        for i in range(n - 1):
            u, v = nodes[i], nodes[i + 1]
            if randint(0, 1):
                u, v = v, u
            edges.append((u, v))

        input = Input(n, m, edges)
        return self.validateAndReturn(input, constraints)

    def an_edge_case(self) -> Input:
        constraints = self.generalConstraints
        n = constraints.n.upper
        m = n - 1
        nodes = list(range(2, n + 1))
        random.shuffle(nodes)
        nodes = [1] + nodes
        edges = []
        for i in range(n - 1):
            u, v = nodes[min(i, 1)], nodes[i + 1]
            if randint(0, 1):
                u, v = v, u
            edges.append((u, v))

        input = Input(n, m, edges)
        return self.validateAndReturn(input, constraints)

    def only_connected_to_first_few(self) -> Input:
        constraints = self.generalConstraints
        n = constraints.n.upper
        m = n - 1
        nodes = list(range(2, n + 1))
        random.shuffle(nodes)
        nodes = [1] + nodes
        edges = []
        for i in range(n - 1):
            u, v = nodes[randint(0, min(i, 10))], nodes[i + 1]
            if randint(0, 1):
                u, v = v, u
            edges.append((u, v))

        input = Input(n, m, edges)
        return self.validateAndReturn(input, constraints)

    ### IMPLEMENT GENERATORS END ###

    def generate(self) -> List[Input]:
        generators = []

        for _ in range(4):
            generators.append(lambda: self.random_small(n_bounds=(1, 10), s1_bounds=(1, 10), s2_bounds=(1, 10), h_bounds=(1, 10), t_bounds=(1, 10), c_bounds=(1, 10)))
        for _ in range(0):
            generators.append(lambda: self.random(n_bounds=(10 + 1, 10**2), m_bounds=(0, 10**3)))
        for _ in range(0):
            generators.append(lambda: self.random(n_bounds=(10**2 + 1, 10**3), m_bounds=(0, 10**4)))
        for _ in range(4):
            generators.append(lambda: self.random(n_bounds=(10**3+1, 10**4), s1_bounds=(1, 10**4), s2_bounds=(1, 10**4), h_bounds=(1, 10**4), t_bounds=(1, 10**4), c_bounds=(1, 10**2)))
        for _ in range(0):
            generators.append(lambda: self.random(n_bounds=(10**4 + 1, 2 * 10**5), m_bounds=(0, 2 * 10**5)))
        for _ in range(4):
            generators.append(lambda: self.random(n_bounds=(5 * 10**4, 10**5), s1_bounds=(5 * 10**4, 10**5), s2_bounds=(5 * 10**4, 10**5), h_bounds=(1, 10**5), t_bounds=(1, 10**5), c_bounds=(4* 10**2, 10**3)))


        #generators.append(lambda: self.random(n_bounds=(2 * 10**5, 2 * 10**5), m_bounds=(0, 0)))

        for _ in range(4):
            generators.append(lambda: self.random(n_bounds=(1, 10), s1_bounds=(1, 10), s2_bounds=(1, 10), h_bounds=(1, 10), t_bounds=(1, 10), c_bounds=(1, 10)))
        for _ in range(0):
            generators.append(lambda: self.connected_random(n_bounds=(10 + 1, 10**2), m_bounds=(0, 10**3)))
        for _ in range(0):
            generators.append(lambda: self.connected_random(n_bounds=(10**2 + 1, 10**3), m_bounds=(0, 10**4)))
        for _ in range(4):
            generators.append(lambda: self.random(n_bounds=(10**3+1, 10**4), s1_bounds=(1, 10**4), s2_bounds=(1, 10**4), h_bounds=(1, 10**4), t_bounds=(1, 10**4), c_bounds=(1, 10**2)))
        for _ in range(0):
            generators.append(lambda: self.connected_random(n_bounds=(10**4 + 1, 2 * 10**5), m_bounds=(0, 2 * 10**5)))
        for _ in range(4):
            generators.append(lambda: self.random(n_bounds=(5 * 10**4, 10**5), s1_bounds=(5 * 10**4, 10**5), s2_bounds=(5 * 10**4, 10**5), h_bounds=(1, 10**5), t_bounds=(1, 10**5), c_bounds=(4* 10**2, 10**3)))


        #generators.append(self.max_chain)
        #generators.append(self.an_edge_case)

        for _ in range(0):
            generators.append(self.only_connected_to_first_few)

        inputs: List[Input] = []
        print("Generating inputs...")
        for generate in tqdm(generators):
            inputs.append(generate())
        return inputs

    def validateAndReturn(self, input: Input, constraints: Constraints):
        constraints.validate(input)
        self.generalConstraints.validate(input)
        return input
