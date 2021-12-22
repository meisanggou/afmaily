# !/usr/bin/env python
# coding: utf-8
import os

__author__ = 'zhouhenglc'


def _get_mode():
    mode = os.environ.get('afamily_mode', 'default')
    return mode


MODE = _get_mode()
