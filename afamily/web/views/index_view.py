# !/usr/bin/env python
# coding: utf-8
from flask_helper.template import RenderTemplate
from flask_helper.view import View

from afamily.utils import load_data


__author__ = 'zhouhenglc'

index_view = View('index_view', __name__)
rt = RenderTemplate()


@index_view.route('/')
def index():
    data = load_data.load_file('annual_events.yaml')
    annual_events = data['annual_events']
    annual_events.reverse()
    return rt.render('timeline.html', annual_events=annual_events)


@index_view.route('/photo')
def photo():
    return rt.render('photo1.html')
