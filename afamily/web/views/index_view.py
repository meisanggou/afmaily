# !/usr/bin/env python
# coding: utf-8
from flask import jsonify
from flask import request
from flask_helper.template import RenderTemplate
from flask_helper.view import View

from afamily.utils import load_data

from afamily.web import helper


__author__ = 'zhouhenglc'

index_view = View('index_view', __name__)
rt = RenderTemplate()
PHOTOS = helper.register_photos()


@index_view.route('/')
def index():

    version = int(request.args.get('version', 2))
    if version not in (1, 2):
        version = 1
    template = 'timeline%s.html' % version
    data = load_data.load_file('annual_events.yaml')
    annual_events = list(data['annual_events'])
    for ae in annual_events:
        for ae_e in ae['events']:
            if 'photo' not in ae_e:
                continue
            if 'album_cover' in ae_e:
                continue
            ae_e['album_cover'] = PHOTOS[ae_e['photo']]['urls'][0][1]
            print(ae_e['album_cover'])
    annual_events.reverse()
    return rt.render(template, annual_events=annual_events)


@index_view.route('/photo')
def photo():
    name = request.args.get('name', 'album2')
    mapping = {'album1': 'photo2', "album2": 'photo2'}
    if name not in PHOTOS:
        name = 'album2'
    url_items = PHOTOS[name]['urls']
    title = PHOTOS[name]['title']
    template = '%s.html' % mapping.get(name, 'photo2')
    return rt.render(template, img_items=url_items, title=title, album_name=name)


@index_view.route('/photo/star', methods=['PUT'])
def star_photo():
    pass
    return jsonify({'status': True, 'data': 'success'})