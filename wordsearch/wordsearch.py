"""
Create a random wordsearch grid and identify words included
"""
import random
import string
import numpy as np

class Matrix:
    """Create a matrix of characters and find all the words included"""

    def __init__(self, matrix_size):
        self.matrix_size = matrix_size
        self.matrix = self.new_matrix()

    def __repr__(self):
        matrix_rows = []

        for _, row in enumerate(self.matrix):
            matrix_rows.append(" ".join(row))

        return "\n".join(matrix_rows)

    def __contains__(self, word):

        if self._find_word_in_row(word) or self._find_word_in_column(word) or self._find_word_in_diagonal(word):
            return True

        return False

    def new_matrix(self):
        """Return a matrix of uppercase characters of height and width self.matrix_size"""

        uppercase_letters = string.ascii_uppercase

        # create a matrix with populated values of '0'
        wordsearch_matrix = np.full((self.matrix_size, self.matrix_size), '0')

        # replace the '0's with random characters from uppercase_letters
        for row_idx, row in enumerate(wordsearch_matrix):
            for col_idx, _ in enumerate(row):
                row[col_idx] = random.choice(uppercase_letters)
            wordsearch_matrix[row_idx] = row

        return wordsearch_matrix

    def _find_word_in_row(self, word):
        """Return True if the word exists in the rows of the matrix, False if it does not"""

        for _, row in enumerate(self.matrix):
            search_string = "".join(row)
            if self._find_word_in_string(search_string, word):
                return True

        return False

    def _find_word_in_column(self, word):
        """Return True if the word exists in the columns of the matrix, False if it does not"""

        for col in range(self.matrix_size):
            search_string = "".join(self.matrix[:, col])
            if self._find_word_in_string(search_string, word):
                return True

        return False

    def _find_word_in_diagonal(self, word):
        """Return True if the word exists in the diagonals of the matrix, False if it does not"""

        for diag in range(self.matrix_size):
            search_string = "".join(np.diagonal(self.matrix, diag))
            if self._find_word_in_string(search_string, word):
                return True

        for diag in range(-1, 0-self.matrix_size, -1):
            search_string = "".join(np.diagonal(self.matrix, diag))
            if self._find_word_in_string(search_string, word):
                return True

        flip_matrix = np.fliplr(self.matrix)
        for diag in range(self.matrix_size):
            search_string = "".join(np.diagonal(flip_matrix, diag))
            if self._find_word_in_string(search_string, word):
                return True

        for diag in range(-1, 0-self.matrix_size, -1):
            search_string = "".join(np.diagonal(flip_matrix, diag))
            if self._find_word_in_string(search_string, word):
                return True

        return False

    def _find_word_in_string(self, search_string, word):
        """Return True if the word exists in the provided string"""

        if (word in search_string) or (word in search_string[::-1]):
            return True

        return False
