"""
Test the wordsearch module
"""
import pytest
from wordsearch.wordsearch import WordSearch

def test_new_matrix():
    """Test creating a new matrix and confirm there are no default values remaining"""

    zeros_exist = False
    word_list = ['SOME', 'SMURFY', 'LIST']
    wordsearch = WordSearch(5, word_list)

    for _, row in enumerate(wordsearch.matrix):
        if '0' in row:
            zeros_exist = True

    assert wordsearch.matrix.shape == (5, 5)
    assert not zeros_exist

def test_finding_words_in_row():
    """Test finding words in a row of a given matrix"""
    word_list = ['YUM', 'BOA', 'YEP']

    wordsearch = WordSearch(3, word_list)

    wordsearch.matrix[0] = ['Y', 'U', 'M']
    wordsearch.matrix[1] = ['A', 'O', 'B']
    wordsearch.matrix[2] = ['M', 'F', 'C']

    wordsearch.words_found = wordsearch.find_words()

    assert 'YUM' in wordsearch.words_found
    assert 'BOA' in wordsearch.words_found
    assert 'YEP' not in wordsearch.words_found
