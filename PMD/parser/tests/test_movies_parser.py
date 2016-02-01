from unittest import TestCase
from PMD.parser.movie_parser import *


class TestMoviesParser(TestCase):
    def test_get_path_name(self):
        self.assertRaises(TypeError, get_path_name, 1)

        file1 = './Epoka Lodowcowa/Epoka Lodowcowa.avi'
        file2 = 'Kły/1x2.mp4'
        file3 = '1x2.mp4'

        self.assertEqual(get_path_name(file1), ('./Epoka Lodowcowa/', 'Epoka Lodowcowa.avi'))
        self.assertEqual(get_path_name(file2), ('Kły/', '1x2.mp4'))
        self.assertEqual(get_path_name(file3), ('/', '1x2.mp4'))

    def test_guessit_parser(self):
        self.assertRaises(TypeError, guessit_parser, 1)

        file1 = './Epoka Lodowcowa/Epoka Lodowcowa.avi'
        file2 = './Kły/Kły.2014.mp4'
        file3 = 'Kły/1x2.mp4'

        dict1 = {'path': './Epoka Lodowcowa/', 'episode': None, 'type': 'movie', 'title': 'Epoka Lodowcowa',
                 'file_name': 'Epoka Lodowcowa.avi', 'series': None, 'season': None, 'year': None}
        dict2 = {'file_name': 'Kły.2014.mp4', 'path': './Kły/', 'title': 'Kły', 'season': None, 'episode': None,
                 'year': 2014, 'type': 'movie', 'series': None}
        dict3 = {'path': 'Kły/', 'file_name': '1x2.mp4', 'title': 'Kły', 'season': 1, 'episode': 2,
                 'year': None, 'type': 'episode', 'series': None}

        self.assertEqual(guessit_parser(file1), Movie(**dict1))
        self.assertEqual(guessit_parser(file2), Movie(**dict2))
        self.assertEqual(guessit_parser(file3), Movie(**dict3))

    def test_movies_parser(self):
        l = ['./Epoka Lodowcowa/Epoka Lodowcowa.avi', './Kły/Kły.2014.mp4']

        dict1 = {'path': './Epoka Lodowcowa/', 'episode': None, 'type': 'movie', 'title': 'Epoka Lodowcowa',
                 'file_name': 'Epoka Lodowcowa.avi', 'series': None, 'season': None, 'year': None}
        dict2 = {'file_name': 'Kły.2014.mp4', 'path': './Kły/', 'title': 'Kły', 'season': None, 'episode': None,
                 'year': 2014, 'type': 'movie', 'series': None}

        par = movies_parser(l)

        self.assertEqual(par[0], Movie(**dict1))
        self.assertEqual(par[1], Movie(**dict2))

        print()
