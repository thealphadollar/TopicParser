"""Module to store all the required classes and associated functions."""
from heapq import nlargest
from typing import List


class Book:
    """Class to store Book object."""

    def __init__(self, name: str, description: str) -> None:
        """
        Construct new Book object.

        :param name: name of the book
        :param description: description of the book
        """
        self.name = name
        self.description = description
        self.genres = dict()

    def get_top_genres(self, num: int = 3) -> List["Genre"]:
        """
        Return top genres for the book if available.

        Genres with scores 0 are not returned even if they are in top 3.

        :param num: number of genres to return
        :return: list of top genres
        """
        # using heap to find top genres among all
        top_genres = nlargest(num, list(self.genres.values()), Genre.get_score)
        top_genres = [genre for genre in top_genres if genre.score != 0]
        return top_genres


class Genre:
    """Class to store Genre object."""

    def __init__(self, name: str) -> None:
        """
        Construct new Genre object.

        :param name: name of the genre
        """
        self.name = name
        self._avgValue = 0
        self._keywordsCount = 0
        self._uniqueKeywordsCount = 0
        self.score = 0

    def update_average(self, keyword: "Keyword", times: int) -> None:
        """
        Find new average with the added element.

        The method also updates the _count by 1

        :param keyword: keyword for the element
        :param times: number of times the keyword is present
        :return: None
        """
        self._avgValue = ((self._avgValue * self._uniqueKeywordsCount) +
                          keyword.points[self.name]) / (self._uniqueKeywordsCount + 1)
        self._uniqueKeywordsCount += 1
        self._keywordsCount = self._keywordsCount + times

    @staticmethod
    def get_score(cls: "Genre") -> int:
        """
        Get the corresponding score.

        :param cls: Genre class to calculate score for
        :return: score
        """
        cls.score = cls._avgValue * cls._keywordsCount
        return cls.score


class Keyword:
    """Class to store Keyword object."""

    def __init__(self, name: str, genre: str, points: int) -> None:
        """
        Construct new Keyword object.

        :param name: name of the keyword
        :param genre: genre the keyword belongs to
        :param points: points of the keyword
        """
        self.name = name
        self.genres = [genre]
        self.points = dict({genre: points})
