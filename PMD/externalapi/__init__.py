import logging

import requests

from PMD.externalapi import ERRORS
from PMD.externalapi.exceptions import ServerError, ClientError

log = logging.getLogger(__name__)


class Interface(object):
    path = None

    @staticmethod
    def get(host, headers=None, params=None):
        if host:
            return requests.get(url=host, params=params, headers=headers)

        return None

    @staticmethod
    def get_data(response, exceptions=False, parse=True):
        if response is None:
            return None

        # Return response, if parse=False
        if not parse:
            return response

        # Check status code, log any errors
        error = False

        if response.status_code < 200 or response.status_code >= 300:
            # Lookup status code in trakt error definitions
            name, desc = ERRORS.get(response.status_code, ("Unknown", "Unknown"))

            log.warning('request failed: %s - "%s" (code: %s)', name, desc, response.status_code)

            if exceptions:
                # Raise an exception (including the response for further processing)
                if response.status_code >= 500:
                    raise ServerError(response)
                else:
                    raise ClientError(response)

            # Set error flag
            error = True

        # Return `None` if we encountered an error, return response data
        if error:
            return None

        # Parse response, return data
        content_type = response.headers.get('content-type')

        if content_type and content_type.startswith('application/json'):
            # Try parse json response
            try:
                data = response.json()
            except Exception as e:
                log.warning('unable to parse JSON response: %s', e)
                return None
        else:
            log.debug('response returned content-type: %r, falling back to raw data', content_type)

            # Fallback to raw content
            data = response.content

        return data
