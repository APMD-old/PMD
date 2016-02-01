# -*- coding: utf-8 -*-

import logging


class RangeFilter(logging.Filter):
    def __init__(self, min=logging.DEBUG, max=logging.CRITICAL):
        super().__init__()
        self.min = min
        self.max = max

    def filter(self, record):
        return self.min <= record.levelno <= self.max
