from test_plus.test import TestCase

from PMD.externalapi.omdbapi import OmdbApi


class TestOMBdApi(TestCase):
    def setUp(self):
        self.api = OmdbApi()

    def test_should_find_exact_movie(self):
        data = DataProvider.full_info()
        self.assertTrue(self.api.query(precise_title=data['title'], year=data['year'], media=data['type']) is not None)

    def test_should_find_movie_no_year(self):
        data = DataProvider.no_year_info()
        self.assertTrue(self.api.query(precise_title=data['title'], year=data['year'], media=data['type']) is not None)

    def test_should_find_movie_no_type(self):
        data = DataProvider.no_type_info()
        self.assertTrue(self.api.query(precise_title=data['title'], year=data['year'], media=data['type']) is not None)

    def test_should_not_find_movie(self):
        data = DataProvider.no_title_info()
        self.assertTrue(
            self.api.query(precise_title=data['title'], year=data['year'], media=data['type']) == 'Invalid query')

    def test_should_get_exact_movie_by_imdbid(self):
        data = DataProvider.imdb_info()
        movie = self.api.query(imdbid=data['imdbid'])
        self.assertTrue(movie['imdb'] == data['imdbid'])

    def test_should_handle_wrong_params(self):
        self.assertTrue(self.api.query() == 'Invalid query')


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
