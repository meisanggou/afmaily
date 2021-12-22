# !/usr/bin/env python
# coding: utf-8
import os
import sys

from PIL import Image

__author__ = 'zhouhenglc'


def img_size(img_path):
    im = Image.open(img_path)
    print(im.size)


def zoom_img(img_path, save_path, width=300):
    im = Image.open(img_path)
    old_w, old_h = im.size
    if old_w > width:
        n_h = int(width / old_w * old_h)
    else:
        width, n_h = old_w, old_h
    n_im = im.resize((width, n_h), Image.ANTIALIAS)
    n_im.save(save_path)


def zoom_img_in_directory(dir_path, zoom_options=(('z', 300), )):
    _options = []
    for option in zoom_options:
        zoom_dir = os.path.join(dir_path, option[0])
        if not os.path.exists(zoom_dir):
            os.mkdir(zoom_dir)
        _options.append((option[0], zoom_dir, option[1]))
    items = os.listdir(dir_path)
    img_extensions = ('jpeg', 'jpg', 'png')
    img_items = []
    for item in items:
        if not item.rsplit('.')[-1] in img_extensions:
            continue
        img_items.append(item)
        for _opt in _options:
            z_path = os.path.join(_opt[1], item)
            if os.path.exists(z_path):
                continue
            zoom_img(os.path.join(dir_path, item), z_path, width=_opt[2])
    return _options, img_items


if __name__ == '__main__':
    # zoom_img('1.png', '2.png')
    if len(sys.argv) > 1:
        img_size(sys.argv[1])
    else:
        zoom_img_in_directory('D:/demo')