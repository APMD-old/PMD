from unittest import TestCase
from PMD.parser.movie_parser import guessit_parser, movies_parser

class TestMovies_parser(TestCase):
    def test_guessit_parser(self):
        self.assertRaises(TypeError,guessit_parser,1)

        file1 = './Epoka Lodowcowa/Epoka Lodowcowa.avi'
        file2 = './Kły/Kły.2014.mp4'
        file3 = 'Kły/1x2.mp4'

        dict1 = {'episode': None, 'type': 'movie', 'title': 'Epoka Lodowcowa', 'series': None, 'season': None, 'year': None}
        dict2 = {'title': 'Kły', 'season': None, 'episode': None, 'year': 2014, 'type': 'movie', 'series': None}
        dict3 = {'title': 'Kły', 'season': 1, 'episode': 2, 'year': None, 'type': 'episode', 'series': None}

        self.assertEqual(guessit_parser(file1),dict1)
        self.assertEqual(guessit_parser(file2),dict2)
        self.assertEqual(guessit_parser(file3),dict3)


    def test_movies_parser(self):
        list = []
        list.append('./Epoka Lodowcowa/Epoka Lodowcowa.avi')
        list.append('./Kły/Kły.2014.mp4')

        dict1 = {'episode': None, 'type': 'movie', 'title': 'Epoka Lodowcowa', 'series': None, 'season': None, 'year': None}
        dict2 = {'title': 'Kły', 'season': None, 'episode': None, 'year': 2014, 'type': 'movie', 'series': None}

        par = movies_parser(list)

        self.assertEqual(par[0],dict1)
        self.assertEqual(par[1],dict2)


        print()
