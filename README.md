# A Python Wordsearch created in One Hour

A wordsearch program created in 61 minutes (plus documentation time). Create a grid of random characters, then find the words from the provided words.txt file in the rows, columns, and diagonals, forwards and backwards.

## Getting Started

Clone this repository

Create a Virtual Environment using [pipenv](https://docs.pipenv.org/en/latest/install/)
```
pipenv --three
```

Install the numpy requirement
```
pipenv install --ignore-pipfile
```

Enter the Virtual Environment
```
pipenv shell
```

To create your own 15 x 15 matrix and print the words found
```
./play_wordgame 15 ./words.txt
```

For help with the command-line arguments
```
./play_wordgame -h
```

To execute the tests
```
pipenv install --dev --ignore-pipfile
python3 -m pytest tests
```
