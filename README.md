# TopicParser

A program made for hiring challenge of BookBub: parses topic based on given information.

## Tools Used

The program is written using Python 3.7.4 (and Pipenv used for virtual environment management) with the following third party libraries:

- [Fire](https://github.com/google/python-fire): For creating the CLI interface.

## How To Run

The application can be run by two methods; python package and standalone pip installment.
Below are the steps to run the program:

1. Install Python 3.7 and Pip
    1. For linux: https://tecadmin.net/install-python-3-7-on-ubuntu-linuxmint/
    2. For windows: https://www.python.org/downloads/
   
   To check installation, use `python --version` 
2. Clone the repository.

### Using Pip Install

3. Use `pip install -e .` in the directory with setup.py
4. Run the program by `genre-parser /path/to/json /path/to/csv`

### Using Python

3. Run the program by `python3 -m genre_parser /path/to/json /path/to/csv`


To know more about the package, use `-h` flag.

## Environment Used

The program has been tested on Debian 10 stable with Python 3.7.4 using the locked
dependencies' versions as in the requirements.txt