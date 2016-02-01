from collections import namedtuple

from guessit import guessit

Movie = namedtuple('Movie', ['path', 'file_name', 'type', 'title', 'year', 'series', 'season', 'episode'])


def get_path_name(file_directories):
    if not isinstance(file_directories, str):
        raise TypeError

    head, sep, tail = file_directories.rpartition("/")
    return head + "/", tail


def guessit_parser(file_directories):
    if not isinstance(file_directories, str):
        raise TypeError

    path, name = get_path_name(file_directories)
    guess = guessit(file_directories)

    return Movie(path, name, guess.get('type', 'unknown'), guess.get('title'), guess.get('year'),
                 guess.get('series', None), guess.get('season', None), guess.get('episode', None))


def movies_parser(directories):
    return [guessit_parser(d) for d in directories]
