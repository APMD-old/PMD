import logging

from PMD.externalapi import Interface

log = logging.getLogger(__name__)


class OmdbApi(Interface):
    def __init__(self):
        self.host = "http://www.omdbapi.com"

    def query(self, imdbid=None, precise_title=None, search=None, media=None, year=None):
        if not imdbid and not search and not precise_title:
            return "Invalid query"
        if imdbid:
            query = {'i': imdbid}
        elif precise_title:
            query = {'t': precise_title}
        elif search:
            query = {'s': search}
        else:
            query = {}

        if media:
            query['type'] = media
        if year:
            query['y'] = year

        response = Interface.get(host=self.host, params=query, headers=None)

        items = self.get_data(response)
        if items.get('Response') == 'False':
            return None
        if items is not None:
            return {'title': items.get('Title'),
                    'year': items.get('Year'),
                    'release_date': items.get('Released'),
                    'is_series': items.get('Type') == 'series',
                    'imdb': items.get('imdbID'),
                    'poster': items.get('Poster'),
                    'genre': items.get('Genre').replace(' ', '').split(',')}
        return None
