# !/usr/bin/env python
# coding: utf-8


__author__ = 'zhouhenglc'


class FileStorage(object):

    def __init__(self, file_path):
        self.file_path = file_path

    def load(self):
        with open(self.file_path, 'r') as r:
            r.read()

    def save(self):
        pass
