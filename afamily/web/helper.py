# !/usr/bin/env python
# coding: utf-8
from flask_helper.utils.registry import DataRegistry

from afamily.utils import config
from afamily.utils import contansts
from afamily.utils import img
from afamily.utils import load_data

__author__ = 'zhouhenglc'


def register_photos():
    dr = DataRegistry.get_instance()
    pl_data = load_data.load_file('photo_location.yaml')
    mode = config.MODE
    if mode not in pl_data:
        mode = 'default'
    albums = pl_data[mode]
    photos = {}
    for name, value in albums.items():
        album_location = value['location']
        z_dir, z_items = img.zoom_img_in_directory(album_location)
        url = '%s/%s' % (contansts.URL_PREFIX_PHOTO, name)
        dr.append(contansts.KEY_STATIC_RE, (url, album_location))
        z_url = '%s/%s' % (url, 'z')
        dr.append(contansts.KEY_STATIC_RE, (z_url, z_dir))
        if 'num' in value:
            z_items = z_items[:value['num']]
        z_urls = []
        for item in z_items:
            _u_item = ('%s/%s' % (url, item), '%s/%s' % (z_url, item))
            z_urls.append(_u_item)
        photos[name] = value
        photos[name]['urls'] = z_urls
    return photos
