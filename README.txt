## Tools Used

The program is written using Python 3.7.4 with the following third party libraries:

- Google Fire (https://github.com/google/python-fire): For creating the CLI interface.

## How To Run

The application can be run by two methods; python package and standalone pip installment.
Below are the steps to run the program:

1. Install Python 3.7 and Pip
    1. For linux: https://tecadmin.net/install-python-3-7-on-ubuntu-linuxmint/
    2. For windows: https://www.python.org/downloads/

   To check installation, use `python --version`

2. Unzip the archive and `cd /path/to/unzipped/directory`

### Using Pip Install

3. Use `pip install -e .` in the directory with setup.py
4. Run the program by `genre-parser /path/to/json /path/to/csv`

### Using Python

3. Install the dependencies using `pip3 install -r requirements.txt`
4. Run the program by `python3 -m genre_parser /path/to/json /path/to/csv`


NOTE: To know more about the package, use `genre-parser -h` or `python3 -m genre_parser -h`.

## Environment Used

The program has been tested on Debian 10 stable with Python 3.7.4 using the locked
dependencies' versions as in the requirements.txt


# Edge Cases

Below is the list of interesting observations and methods used to solve the problem more efficiently.

1. Object Oriented Programming has been used to keep the code clean and intuitive. It is further complemented by Python
    docstrings that make it easier to document methods in python. Modern python techniques such as Annotations and Typing
    is used to overcome the shortfall of python being dynamically typed.
2. We've used dictionary to store objects wherever a large number of accesses need to be made. This is done in order to
    keep the access time minimal as Dictionaries are hashed.
3. The complexity of the problem is increased as each keyword may belong to multiple genres and in this scenario, a more
    efficient method of finding the keywords in the description could not be found. I had to resort to plain str.find()
    python method.
4. Python packaging has been done for the easy installation and distribution of the application. I feel it is a little
    bit overkill for the project but since it was asked to make it production ready, this is it.
5. With more time, I could have easily used Docker and made this into a docker image which would have further improved
    the production capability and scalability as well as made it system independent.

NOTE: Most of the codebase is self explanatory and it has been avoided to add unnecessary comments in between code.

# Time taken

It took me around 3 hours to write the algorithm and another 2 hours to do the packaging and researching for the best
package to implement Command Line Interface in python.
