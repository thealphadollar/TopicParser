"""Module to store GenreFinder class."""
import csv
import json

from genre_parser.constants import *
from genre_parser.objects import Book, Genre, Keyword


class GenreFinder:
    """Driving class to find genre of the books from description."""
    def __init__(self) -> None:
        """Constructor for GenreFinder."""
        self.keywords = dict()
        self.books = list()

    def find_genre(self) -> None:
        """Find top three genres for each book."""
        for book_index, book in enumerate(self.books):
            print(book.name)
            for keyword in self.keywords.values():
                keyword_count = book.description.count(keyword.name)
                if keyword_count != 0:
                    for genre in keyword.genres:
                        self.books[book_index].genres[genre] = self.books[
                            book_index
                        ].genres.get(genre, Genre(genre))
                        self.books[book_index].genres[genre].update_average(keyword, keyword_count)

            for genre in book.get_top_genres():
                print(f"{genre.name}, {genre.score}")

    def get_keywords(self, path_to_csv: str) -> None:
        """
        Populate keywords from provided CSV file.

        :param path_to_csv: path to the CSV file
        :return: None
        """
        with open(path_to_csv, 'r') as csvFile:
            data = csv.DictReader(csvFile)

            for value in data:
                # if keyword is not present already
                if self.keywords.get(value[CSV_KEYWORD_KEY].lstrip()) is None:
                    # removing beginning white space from keyword name and weights
                    self.keywords[value[CSV_KEYWORD_KEY].lstrip()] = Keyword(value[CSV_KEYWORD_KEY].lstrip(),
                                                                             value[CSV_GENRE_KEY].lstrip(),
                                                                             int(value[CSV_POINTS_KEY].lstrip()))
                # if keyword already present, just add genre and it's points
                else:
                    # removing beginning white space from keyword name and weights
                    self.keywords[value[CSV_KEYWORD_KEY].lstrip()].genres.append(value[CSV_GENRE_KEY].lstrip())
                    self.keywords[value[CSV_KEYWORD_KEY].lstrip()].points[
                        value[CSV_GENRE_KEY].lstrip()
                    ] = int(value[CSV_POINTS_KEY].lstrip())

    def get_books(self, path_to_json: str) -> None:
        """
        Populate books from provided JSON file.

        :param path_to_json: path to the JSON file
        :return: None
        """
        with open(path_to_json, 'r') as jsonFile:
            data = json.load(jsonFile)

        for value in data:
            self.books.append(Book(value.get(JSON_BOOK_NAME_KEY), value.get(JSON_BOOK_DESC_KEY)))

        self.books = sorted(self.books, key=lambda book: book.name)

    def _reset(self) -> None:
        """Reset the GenreFinder to initial values for next book."""
        for keyword in self.keywords.values():
            keyword.hasOccurred = False
        self.genres = dict()
