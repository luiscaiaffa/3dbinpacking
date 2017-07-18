# -*- coding: utf-8 -*-
from action import Action
from exception import RequiredParameters


class Container(Action):

    def single(self, data):
        url = self.api.get_url(['packer/pack'])
        return super(Container, self).send(url, data)

    def multi(self, data):
        url = self.api.get_url(['packer/packIntoMany'])
        return super(Container, self).send(url, data)

    def find(self, data):
        url = self.api.get_url(['packer/findSmallestBin'])
        return super(Container, self).send(url, data)

    def adjustment(self, data):
        url = self.api.get_url(['packer/findBinSize'])
        return super(Container, self).send(url, data)

    def maximum(self, data):
        url = self.api.get_url(['packer/fillContainer'])
        return super(Container, self).send(url, data)

   