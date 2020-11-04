#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ライブラリのインポート
import numpy as np
import cv2
import library

# 配列を作成
image = np.zeros((210, 210, 3))

# 縦の線を書く
for i in range(0, 210):
    for j in range(100, 110):
        library.draw(image, i, j, 108, 52, 36)

# 横の線を書く
for i in range(0, 210):
    for j in range(100, 110):
        library.draw(image, j, i, 118, 46, 5)

# 左上の枠に色を塗る
for i in range(0, 100):
    for j in range(0, 100):
        library.draw(image, i, j, 242, 160, 161)

# 右上の枠に色を塗る
for i in range(0, 100):
    for j in range(110, 210):
        library.draw(image, i, j, 238, 120, 0)

# 左下の枠に色を塗る
for i in range(110, 210):
    for j in range(0, 100):
        library.draw(image, i, j, 145, 115, 71)

# 右下の枠に色を塗る
for i in range(110, 210):
    for j in range(110, 210):
        library.draw(image, i, j, 187, 200, 230)


# 画像を保存
cv2.imwrite("practice.png", image)
# 保存した画像を表示
image = cv2.imread("practice.png")
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
