# -*- coding: utf-8 -*-
from packing import default_api

class Action(object):

    def __init__(self):
        self.api = default_api()

    def send(self, url, data):
        return self.api.post(url, data)

    
