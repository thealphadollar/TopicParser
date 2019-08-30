import fire

from src.genreFinder import GenreFinder


def main(path_to_books_json: str, path_to_keywords_csv: str) -> None:
    """
    Find genre of the books using the provided keywords and the corresponding points.

    :param path_to_books_json: relative path to JSON file containing information about books
    :param path_to_keywords_csv: relative path to CSV file containing the keywords with associated points and genre
    :return: None
    """
    genre_finder = GenreFinder()
    # load books
    genre_finder.get_books(path_to_books_json)
    # load keywords
    genre_finder.get_keywords(path_to_keywords_csv)
    # find top genres and print
    genre_finder.find_genre()


if __name__ == "__main__":
    fire.Fire(main)
