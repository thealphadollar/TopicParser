import sys
from distutils.core import setup

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 6)

# This check and everything above must remain compatible with Python 3.6.
if CURRENT_PYTHON < REQUIRED_PYTHON:
    sys.stderr.write("""
==========================
Unsupported Python version
==========================
This version of GenreFinder requires Python {}.{}, but you're trying to
install it on Python {}.{}.
""".format(*(REQUIRED_PYTHON + CURRENT_PYTHON)))
    sys.exit(1)

setup(
    name='genre_parser',
    version='0.1',
    packages=['genre_parser'],
    url='https://thealphadollar.me',
    license='MIT',
    author='Shivam Kumar Jha',
    author_email='kingshivam99@gmail.com',
    install_requires=[
        "fire==0.2.1",
        "isort==4.3.21",
        "mypy==0.720",
        "mypy-extensions==0.4.1",
        "pycodestyle==2.5.0",
        "pydocstyle==4.0.1",
        "six==1.12.0",
        "snowballstemmer==1.9.0",
        "termcolor==1.1.0",
        "typed-ast==1.4.0",
        "typing-extensions==3.7.4"
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Intended Audience :: BookBub/Developers',
        'Operating System :: POSIX :: Linux',
        'Topic :: Utilities',
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': ['genre-parser=genre_parser.__main__:entry_point']
    },
    description='find the genre of books based on it\'s description and keywords provided'
)
