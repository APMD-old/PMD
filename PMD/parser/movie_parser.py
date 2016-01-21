from guessit import guessit

def guessit_parser(fileName):
    if not isinstance(fileName, str):
        raise TypeError

    guess = guessit(fileName)

    dictionary = {}
    dictionary["type"] = guess.get("type","unknown")
    dictionary["title"] = guess.get("title")
    dictionary["year"] = guess.get("year")
    dictionary["series"] = guess.get("series")
    dictionary["season"] = guess.get("season")
    dictionary["episode"] = guess.get("episode")

    return dictionary

def movies_parser(directories):
    list = []
    for dir in directories:
        list.append(guessit_parser(dir))

    return list






