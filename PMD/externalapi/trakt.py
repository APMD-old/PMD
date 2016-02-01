import logging

from . import Interface

log = logging.getLogger(__name__)


class Trakt(Interface):
    def __init__(self, context):
        self.host = "http://api-v2launch.trakt.tv"
        self.context = context
        self.headers = {'Content-Type': 'my-app/0.0.1',
                        'trakt-api-key': '0e94d9d043263c9c8c09815d80b8d7378cfe1ec2c0fee4a1ac500e90e073f235',
                        'trakt-api-version': '2'}

    def query(self, query, media=None, year=None, **kwargs):
        query = {
            'query': query
        }

        if media:
            query['type'] = media

        if year:
            query['year'] = year

        response = self.get(self.host + self.context, headers=self.headers, params=query)

        items = self.get_data(response, **kwargs)

        if items is not None:
            items = items[0]
            return {'title': items.get('movie').get('title'),
                    'year': items.get('movie').get('year'),
                    'release_date': items.get('movie').get('released'),
                    'is_series': items.get('type') == 'series',
                    'imdb': items.get('movie').get('ids').get('imdb')}

        return None
