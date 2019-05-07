"""
Create a random wordsearch grid and identify words included
"""
import random
import string
import numpy as np

class WordSearch:
    """Create a matrix of characters and find all the words included"""

    def __init__(self, matrix_size, words_to_find):
        self.matrix_size = matrix_size
        self.matrix = self.new_matrix()
        self.words_to_find = words_to_find

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