#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ライブラリのインポート
import cv2
import numpy as np


# 空白画像を作成
white_image = np.ones((200, 300, 3), np.uint8) * 255

# バウンディングボックスを描画
cv2.rectangle(white_image,(30, 50), (150, 150),(0, 0, 255), 2)

# 画像を表示
cv2.imshow("White Image", white_image)
cv2.waitKey(0)
cv2.destroyAllWindows()