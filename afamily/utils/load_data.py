# !/usr/bin/env python
# coding: utf-8
import functools
import os
import yaml

__author__ = 'zhouhenglc'

_path = os.path.abspath(__file__)
_dir = os.path.dirname(_path)
_data_dir = os.path.abspath(os.path.join(_dir, '../data'))
ENCODING = 'utf-8'
_CACHE = {}


def cache(f):
    @functools.wraps(f)
    def _func(*args, **kwargs):
        if args[0] in _CACHE:
            return _CACHE[args[0]]
        r = f(*args, **kwargs)
        _CACHE[args[0]] = r
        return r
    return _func


def load_yaml_file(content):
    return yaml.load(content, yaml.FullLoader)


@cache
def load_file(name, reload=False):
    path = os.path.join(_data_dir, name)
    _loader = lambda x: x
    if name.endswith('.yaml'):
        _loader = load_yaml_file
    with open(path, encoding=ENCODING) as r:
        c = r.read()
        return _loader(c)


@cache
def list_files(dir_name):
    items = os.listdir(dir_name)
    return items


if __name__ == '__main__':
    o = load_file('annual_events.yaml')
    print(o)
    o2 = load_file('annual_events.yaml')
    print(o2)
