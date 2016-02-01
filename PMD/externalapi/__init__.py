import logging

import requests
from datetime import date, datetime

from .errors import ERRORS
from .exceptions import ServerError, ClientError

log = logging.getLogger(__name__)


class Interface(object):
    date_format = None

    @staticmethod
    def get(host, headers=None, params=None):
        if host:
            return requests.get(url=host, params=params, headers=headers)

        return None

    @staticmethod
    def get_data(response, exceptions=False, parse=True):
        if response is None:
            return None

        if not parse:
            return response

        error = False

        if response.status_code < 200 or response.status_code >= 300:
            name, desc = ERRORS.get(response.status_code, ("Unknown", "Unknown"))

            log.warning('request failed: %s - "%s" (code: %s)', name, desc, response.status_code)

            if exceptions:
                if response.status_code >= 500:
                    raise ServerError(response)
                else:
                    raise ClientError(response)
            error = True

        if error:
            return None

        content_type = response.headers.get('content-type')

        if content_type and content_type.startswith('application/json'):
            try:
                data = response.json()
            except Exception as e:
                log.warning('unable to parse JSON response: %s', e)
                return None
        else:
            log.debug('response returned content-type: %r, falling back to raw data', content_type)
            data = response.content

        return data

    @classmethod
    def parse_date(cls, date_string):
        try:
            return datetime.strptime(date_string, cls.date_format).date()
        except ValueError:
            return None
