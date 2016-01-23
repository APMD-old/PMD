import logging

from PMD.externalapi import Interface

log = logging.getLogger(__name__)


class OmdbApi(Interface):
    def __init__(self):
        self.host = "http://www.omdbapi.com"

    def query(self, imdbid=None, precise_title=None, search=None, media=None, year=None, **kwargs):
        if not imdbid and not search and not precise_title:
            return "Invalid query"
        if imdbid:
            query = {'i': imdbid}
        elif precise_title:
            query = {'t': precise_title}
        elif search:
            query = {'s': search}

        # Set optional parameters
        if media:
            query['type'] = media

        if year:
            query['y'] = year

        if kwargs:
            for key in kwargs.keys():
                query[key] = kwargs.get(key)

        # Send request
        response = Interface.get(host=self.host, params=query, headers=None)
        # Parse response
        items = self.get_data(response, **kwargs)
        if items.get('Response') == 'False':
            return None
        if items is not None:
            return {'title': items.get('Title'),
                    'year': items.get('Year'),
                    'release_date': items.get('Released'),
                    'is_series': items.get('Type') == 'series',
                    'imdb': items.get('imdbID'),
                    'poster': items.get('Poster')}

        return None


def main():
    movie = OmdbApi()
    resp = movie.query(precise_title='Batman', media='Movie', year='2015')
    print(resp)


if __name__ == '__main__':
    main()
