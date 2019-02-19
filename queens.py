import numpy as np


class QueensSolver:
    def __init__(self, size=8, quiet=False):
        self.unique_solutions = 0
        self.size = size
        self.quiet = quiet
        self.rows = [-1] * self.size

        self.symmetric_solutions = set()

    def solve(self):
        if self.size == 1:
            return 1, 1

        self.put_q(0)
        return len(self.symmetric_solutions), self.unique_solutions

    def print_res(self, msg=''):
        if self.quiet:
            return

        for row in range(self.size):
            for col in range(self.size):
                print(' Q ' if col == self.rows[row] else ' . ', end='', )
            print()
        print(f'{msg}'.center(self.size * 3), end='\n\n')

    def check(self, i, j):
        for col in range(i):
            if any((self.rows[col] == j,  # vertical
                    self.rows[col] - col == j - i,  # \ diag
                    self.rows[col] + col == j + i,  # / diag
                    )):
                return False
        return True

    def _convert_matrix(self, matrix):
        return tuple(r.argmax() for r in matrix)

    def _rot360(self, matrix):
        matrix = np.rot90(matrix)
        self.symmetric_solutions.add(self._convert_matrix(matrix))

        matrix = np.rot90(matrix)
        self.symmetric_solutions.add(self._convert_matrix(matrix))

        matrix = np.rot90(matrix)
        self.symmetric_solutions.add(self._convert_matrix(matrix))

        matrix = np.rot90(matrix)
        self.symmetric_solutions.add(self._convert_matrix(matrix))

    def generate_sym_solutions(self):
        matrix = np.zeros((self.size, self.size), np.int8)

        for row, col in enumerate(self.rows):
            matrix[row, col] = 1

        self._rot360(matrix)

        matrix = np.fliplr(matrix)
        self._rot360(matrix)

        matrix = np.flipud(matrix)
        self._rot360(matrix)

    def put_q(self, i):
        if i == self.size:
            if tuple(self.rows) in self.symmetric_solutions:
                return
            self.generate_sym_solutions()

            self.unique_solutions += 1
            self.print_res(f'Solution #{self.unique_solutions}')
            return

        for j in range(self.size):
            if self.check(i, j):
                self.rows[i] = j
                self.put_q(i + 1)


for queens in range(10):
    solver = QueensSolver(queens + 1, True)
    solutions, unique = solver.solve()
    print(f'{queens + 1} queens has {solutions} solutions ({unique} unique)')
