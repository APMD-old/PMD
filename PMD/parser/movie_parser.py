from guessit import guessit


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

    dictionary = {}
    dictionary["path"] = path
    dictionary["file_name"] = name
    dictionary["type"] = guess.get("type", "unknown")
    dictionary["title"] = guess.get("title")
    dictionary["year"] = guess.get("year")
    dictionary["series"] = guess.get("series")
    dictionary["season"] = guess.get("season")
    dictionary["episode"] = guess.get("episode")

    return dictionary


def movies_parser(directories):
    l = []
    for d in directories:
        l.append(guessit_parser(d))

    return l






