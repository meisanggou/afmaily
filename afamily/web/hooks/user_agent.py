# !/usr/bin/env python
# coding: utf-8
from flask import g
from flask import request

from flask_helper.flask_hook import FlaskHook

__author__ = 'zhouhenglc'


class UserAgentHook(FlaskHook):
    KEY = 'User-Agent'
    priority = 200

    def before_request(self):
        g.wx_browser = False

        user_agent = request.headers.get(self.KEY, None)
        print(user_agent)
        if not user_agent:
            return
        if 'MicroMessenger' in user_agent:
            g.wx_browser = True
            print('is true')