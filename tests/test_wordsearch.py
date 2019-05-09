"""
Test the wordsearch module
"""
#pylint: disable=redefined-outer-name
import numpy
import pytest
from wordsearch.wordsearch import Matrix


@pytest.fixture
def testable_wordsearch():
    """Create a test matrix to be used in future tests"""

    testable_matrix = numpy.asarray(
        [['Y', 'U', 'M'],
         ['A', 'O', 'B'],
         ['M', 'F', 'C']]
    )

    wordsearch = Matrix(3, testable_matrix)

    return wordsearch

def test_new_matrix():
    """Test creating a new matrix and confirm there are no default values remaining"""

    wordsearch = Matrix(5)

    assert '0' not in wordsearch

def test_finding_words_in_row(testable_wordsearch):
    """Test finding words in a row of a given matrix"""

    assert 'YUM' in testable_wordsearch
    assert 'BOA' in testable_wordsearch
    assert 'YEP' not in testable_wordsearch

def test_finding_words_in_column(testable_wordsearch):
    """Test finding words in a column of a given matrix"""

    assert 'YAM' in testable_wordsearch
    assert 'CBM' in testable_wordsearch
    assert 'GUY' not in testable_wordsearch

def test_finding_words_in_diagonals(testable_wordsearch):
    """Test finding words in the diagonals of a given matrix"""

    assert 'MOM' in testable_wordsearch
    assert 'UB' in testable_wordsearch
    assert 'DAD' not in testable_wordsearch

def test_printing_wordsearch(testable_wordsearch, capsys):
    """Test printing the WordSearch object"""

    print(testable_wordsearch)
    captured = capsys.readouterr()

    assert captured.out == "Y U M\nA O B\nM F C\n"
    assert captured.err == ''
