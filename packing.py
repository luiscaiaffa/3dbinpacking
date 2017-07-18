# -*- coding: utf-8 -*-
import os, re, json, requests
from requests.auth import HTTPBasicAuth


class Packing(object):

    def __init__(self, username, api_key):
        self.username = username 
        self.api_key = api_key

    def headers(self):
        return {
            "Content-type": "application/x-www-form-urlencoded",
            "Accept": "text/plain"
        }

    def base_request(self, url, method, data={}):
        try:
            data['username'] = self.username
            data['api_key'] = self.api_key
            response = requests.request(method, url,
                                        data=json.dumps(data),
                                        headers=self.headers())
            return json.loads(response.content.decode('utf-8'))
        except Exception as error:
            raise

    def get(self, url, data={}):
        return self.base_request(url, 'GET', data=data)

    def post(self, url, data={}):
        return self.base_request(url, 'POST', data=data)


    def get_url(self, paths):
        url = 'https://global-api.3dbinpacking.com/'
        for path in paths:
            url = re.sub(r'/?$', re.sub(r'^/?', '/', str(path)), url)
        return url


__default_api__ = None


def default_api():

    global __default_api__
    if __default_api__ is None:
        __default_api__ = Packing(username='caiaffa', api_key='6c8917ae41b340b2015119760d9f4035')
    return __default_api__

