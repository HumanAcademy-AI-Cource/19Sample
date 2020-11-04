#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ライブラリのインポート
import numpy as np

def draw(image, x, y, r, g, b):
    '''
    ピクセルに色を塗る関数
    '''
    image[x][y][0] = b
    image[x][y][1] = g
    image[x][y][2] = r
