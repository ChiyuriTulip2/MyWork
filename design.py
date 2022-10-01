#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

def tag():
    tag = ["フィルタ", "トーン変更", "モザイク加工"]
    return random.choice(tag)
title = tag()

def tag_filter():
    tag_filter = ["デッサン風", "ラップ加工", "ぼかし加工", "波形挿入", "ジグザグ挿入"]
    return random.choice(tag_filter)
title_filter = tag_filter()

def tag_tone():
    tag_tone = ["彩度", "明度", "明るさ", "コントラスト", "露光量"]
    return random.choice(tag_tone)
title_tone = tag_tone()

def tag_mosaic():
    tag_mosaic = ["パッチワーク", "ハーフトーン", "ベーシック模様", "スキン模様", "装飾模様"]
    return random.choice(tag_mosaic)
title_mosaic = tag_mosaic()

if title == "フィルタ":
    print(title)
    print(title_filter)

elif title == "トーン変更":
    print(title)
    print(title_tone)

elif title == "モザイク加工":
    print(title)
    print(title_mosaic)

# In[ ]:
