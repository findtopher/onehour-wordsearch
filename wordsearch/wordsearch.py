"""
Create a random wordsearch grid and identify words included
"""
import random
import string
import numpy as np

class Matrix:
    """Create a matrix of characters and find all the words included"""

    def __init__(self, matrix_size, matrix=None):
        self._matrix_size = matrix_size

        if (matrix is not None) and (isinstance(matrix, np.ndarray)):
            if matrix.shape == (self._matrix_size, self._matrix_size):
                self._matrix = matrix
            else:
                raise ValueError('Matrix argument matrix_size must match matrix argument')
        elif matrix is not None:
            raise TypeError('Matrix argument matrix must be a numpy ndarray object')
        else:
            self._matrix = self._random_matrix()

        self._matrix_strings = self._matrix_to_strings()

    def __repr__(self):
        matrix_rows = []

        for _, row in enumerate(self._matrix):
            matrix_rows.append(" ".join(row))

        return "\n".join(matrix_rows)

    def __contains__(self, word):

        for matrix_string in self._matrix_strings:
            if (word in matrix_string) or (word in matrix_string[::-1]):
                return True

        return False

    def _random_matrix(self):
        """Return a matrix of uppercase characters of height and width self._matrix_size"""

        uppercase_letters = string.ascii_uppercase

        # create a matrix with populated values of '0'
        wordsearch_matrix = np.full((self._matrix_size, self._matrix_size), '0')

        # replace the '0's with random characters from uppercase_letters
        for row_idx, row in enumerate(wordsearch_matrix):
            for col_idx, _ in enumerate(row):
                row[col_idx] = random.choice(uppercase_letters)
            wordsearch_matrix[row_idx] = row

        return wordsearch_matrix

    def _matrix_to_strings(self):
        """Return a list of strings that represent the rows, columns, and diagonals of the matrix"""

        matrix_strings = self._generate_row_strings()
        matrix_strings.extend(self._generate_column_strings())
        matrix_strings.extend(self._generate_diagonal_strings())

        return matrix_strings

    def _generate_row_strings(self):
        """Return a list of strings that represent the rows in the matrix"""

        row_strings = []

        for _, row in enumerate(self._matrix):
            row_strings.append("".join(row))

        return row_strings

    def _generate_column_strings(self):
        """Return a list of strings that represent the columns in the matrix"""

        column_strings = []

        for col in range(self._matrix_size):
            column_strings.append("".join(self._matrix[:, col]))

        return column_strings

    def _generate_diagonal_strings(self):
        """Return True if the word exists in the diagonals of the matrix, False if it does not"""

        diagonal_strings = []

        for diag in range(self._matrix_size):
            diagonal_strings.append("".join(np.diagonal(self._matrix, diag)))

        for diag in range(-1, 0-self._matrix_size, -1):
            diagonal_strings.append("".join(np.diagonal(self._matrix, diag)))

        flip_matrix = np.fliplr(self._matrix)
        for diag in range(self._matrix_size):
            diagonal_strings.append("".join(np.diagonal(flip_matrix, diag)))

        for diag in range(-1, 0-self._matrix_size, -1):
            diagonal_strings.append("".join(np.diagonal(flip_matrix, diag)))

        return diagonal_strings
