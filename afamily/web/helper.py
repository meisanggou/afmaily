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
        # 处理压缩 略缩图 1080p
        zoom_options = (('z', 300), ('1080p', 1080))
        opts, z_items = img.zoom_img_in_directory(album_location,zoom_options)
        url = '%s/%s' % (contansts.URL_PREFIX_PHOTO, name)
        dr.append(contansts.KEY_STATIC_RE, (url, album_location))
        if 'num' in value:
            z_items = z_items[:value['num']]
        z_urls = []
        for opt in opts:
            _zn, z_dir, _ = opt
            z_url = '%s/%s' % (url, _zn)
            dr.append(contansts.KEY_STATIC_RE, (z_url, z_dir))
            z_urls.append(z_url)

        urls = []
        for item in z_items:
            _u_item = [item, '%s/%s' % (url, item)]
            for z_url in z_urls:
                _u_item.append('%s/%s' % (z_url, item))
            urls.append(_u_item)
        photos[name] = value
        photos[name]['urls'] = urls
    return photos
