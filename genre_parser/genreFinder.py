"""Module to store GenreFinder class."""
import csv
import json

from genre_parser.constants import *
from genre_parser.objects import Book, Genre, Keyword
from urllib import request
from genre_parser.constants import BOOKS_ENDPOINT_PAGED


class GenreFinder:
    """Driving class to find genre of the books from description."""

    def __init__(self) -> None:
        """Construct new GenreFinder object."""
        self.keywords = dict()
        self.books = list()

    def find_genre(self) -> None:
        """Find top three genres for each book."""
        # iterate through each book
        for book_index, book in enumerate(self.books):
            # print(book.name)
            for keyword in self.keywords.values():
                # find number of times the keyword is present in the description
                keyword_count = book.description.count(keyword.name)
                if keyword_count != 0:
                    for genre in keyword.genres:
                        # if genre is already added to book, use it
                        # create new Genre object otherwise
                        self.books[book_index].genres[genre] = self.books[
                            book_index
                        ].genres.get(genre, Genre(genre))
                        # update average of the genre
                        self.books[book_index].genres[genre].update_average(keyword, keyword_count)

            # for genre in book.get_top_genres():
            #     print(f"{genre.name}, {int(genre.score)}")

    def top_genre_across(self) -> None:
        """
        Print the top genre across all books

        :return: None
        """
        genres = {}
        for book in self.books:
            for genre in book.genres.values():
                cur_value = genres.get(genre.name)
                if cur_value is None:
                    cur_value = 0
                genres[genre.name] = cur_value + genre.get_score(genre)

        max_genre = None
        max_genre_score = -1e10
        for genre in genres.keys():
            print(f"Genre: {genre} has the score: {genres[genre]}")
            if genres[genre] > max_genre_score:
                max_genre = genre
                max_genre_score = genres[genre]

        print(f"The {max_genre} has highest score of {max_genre_score}")

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
                    self.keywords[value[CSV_KEYWORD_KEY].lstrip()] = Keyword(
                        value[CSV_KEYWORD_KEY].lstrip(),
                        value[CSV_GENRE_KEY].lstrip(),
                        int(value[CSV_POINTS_KEY].lstrip())
                    )
                # if keyword already present, just add genre and it's points
                else:
                    # removing beginning white space from keyword name and weights
                    self.keywords[value[CSV_KEYWORD_KEY].lstrip()].genres.append(
                        value[CSV_GENRE_KEY].lstrip()
                    )
                    self.keywords[value[CSV_KEYWORD_KEY].lstrip()].points[
                        value[CSV_GENRE_KEY].lstrip()
                    ] = int(value[CSV_POINTS_KEY].lstrip())

    def get_books(self, path_to_json=None) -> None:
        """
        Populate books from provided JSON file.

        :param path_to_json: path to the JSON file
        :return: None
        """
        if path_to_json is not None:
            with open(path_to_json, 'r') as jsonFile:
                data = json.load(jsonFile)

        # take from endpoint if path not provided
        else:
            data = list()
            cur_page = 72
            while True:
                print(f"getting response from page number {cur_page}")
                response = request.urlopen(BOOKS_ENDPOINT_PAGED+str(cur_page))
                resp_data = json.loads(response.read())
                print(f"response received from page number {cur_page}")
                if len(resp_data) == 0:
                    break
                data.extend(resp_data)
                cur_page += 1

        print(f"Total number of books fetched are {len(data)}")

        for value in data:
            self.books.append(Book(
                value.get(JSON_BOOK_NAME_KEY),
                value.get(JSON_BOOK_DESC_KEY))
            )

        self.books = sorted(self.books, key=lambda book: book.name)
