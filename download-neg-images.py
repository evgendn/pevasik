#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 11:42:56 2018

@author: KaranJaisingh
"""

import cv2
from six.moves import urllib
import numpy as np
import os
import requests

def store_raw_images():
    neg_image_link = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02823428'
    neg_image_urls = requests.get(neg_image_link).text

    if not os.path.exists('images'):
        os.makedirs('images')

    pic_num = 1

    for i in neg_image_urls.split('\n'):
        try:
            print(str(pic_num) + ": " + i)
            img_data = requests.get(i, timeout=5).content
            with open('images/'+str(pic_num)+'.jpg', 'wb') as handler:
                handler.write(img_data)
            img = cv2.imread('images/'+str(pic_num)+'.jpg', cv2.IMREAD_GRAYSCALE)
            resized_image = cv2.resize(img, (100, 100))
            cv2.imwrite('images/'+str(pic_num)+'.jpg', resized_image)
            pic_num += 1

        except Exception as e:
            print(str(e))

store_raw_images()
