from test_plus.test import TestCase

from ..trakt import Trakt


class TestTraktApi(TestCase):
    def setUp(self):
        self.api = Trakt(context='/search')

    def test_should_find_exact_movie(self):
        data = DataProvider.full_info()
        self.assertIsNotNone(self.api.query(query=data['title'], year=data['year'], media=data['type']))

    def test_should_find_movie_no_year(self):
        data = DataProvider.no_year_info()
        self.assertIsNotNone(self.api.query(query=data['title'], year=data['year'], media=data['type']))

    def test_should_find_movie_no_type(self):
        data = DataProvider.no_type_info()
        self.assertIsNotNone(self.api.query(query=data['title'], year=data['year'], media=data['type']))

    def test_should_not_find_movie(self):
        data = DataProvider.no_title_info()
        self.assertIsNone(self.api.query(query=data['title'], year=data['year'], media=data['type']))


class DataProvider:
    @staticmethod
    def full_info():
        return {'title': 'Batman v Superman: Dawn of Justice', 'year': '2016', 'type': 'movie'}

    @staticmethod
    def no_type_info():
        return {'title': 'Batman v Superman: Dawn of Justice', 'year': '2016', 'type': None}

    @staticmethod
    def no_year_info():
        return {'title': 'Batman v Superman: Dawn of Justice', 'year': None, 'type': 'movie'}

    @staticmethod
    def only_title_info():
        return {'title': 'Batman v Superman: Dawn of Justice', 'year': None, 'type': None}

    @staticmethod
    def no_title_info():
        return {'title': None, 'year': '2016', 'type': 'movie'}

    @staticmethod
    def imdb_info():
        return {'imdbid': 'tt5241796'}
