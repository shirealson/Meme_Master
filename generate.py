#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
import cv2
import numpy as np
import matplotlib.pyplot as plt
import time
def generateWithTemplate(template_path,sentence):

    path = template_path
    save_path = 'generate_img/' + str(time.time())+ '.jpg'


    img = Image.open(path).convert('RGB')
    img_mat = np.asarray(img, np.uint8)
    shape = img_mat.shape
    white = np.ones((30,shape[1],shape[2]), np.uint8)*255
    img_con = np.concatenate((img_mat, white), axis=0)
    img = Image.fromarray(img_con)
    img.save(save_path)



    im = Image.open(save_path)

    w, h = im.size

    imgn = cv2.imread(save_path)
    cv2img = cv2.cvtColor(imgn, cv2.COLOR_BGR2RGB)
    pilimg = Image.fromarray(cv2img)


    draw = ImageDraw.Draw(pilimg)
    font = ImageFont.truetype("simhei.ttf", 20, encoding="utf-8")
    x_pos = w/2 - len(sentence) * 20 / 2 #居中公式
    draw.text((x_pos, h-30), sentence, (0, 0, 0), font=font)#在矩阵绘制文字
 

    cv2charimg = cv2.cvtColor(np.array(pilimg), cv2.COLOR_RGB2BGR)
    # cv2.imshow("ͼƬ", cv2charimg)
    img = Image.fromarray(cv2charimg)
    img.save(save_path)
    return save_path
