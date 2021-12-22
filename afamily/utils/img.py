# !/usr/bin/env python
# coding: utf-8
import os
from PIL import Image

__author__ = 'zhouhenglc'


def zoom_img(img_path, save_path, width=300):
    im = Image.open(img_path)
    old_w, old_h = im.size
    n_h = int(width / old_w * old_h)
    n_im = im.resize((width, n_h))
    n_im.save(save_path)


def zoom_img_in_directory(dir_path):
    zoom_dir = os.path.join(dir_path, 'z')
    if not os.path.exists(zoom_dir):
        os.mkdir(zoom_dir)
    items = os.listdir(dir_path)
    img_extensions = ('jpeg', 'jpg', 'png')
    img_items = []
    for item in items:
        if not item.rsplit('.')[-1] in img_extensions:
            continue
        img_items.append(item)
        z_path = os.path.join(zoom_dir, item)
        if os.path.exists(z_path):
            continue
        zoom_img(os.path.join(dir_path, item), z_path)
    return zoom_dir, img_items


if __name__ == '__main__':
    # zoom_img('1.png', '2.png')
    zoom_img_in_directory('D:/demo')