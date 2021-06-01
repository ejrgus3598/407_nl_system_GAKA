# 조도값 측정, DB에 누적

import numpy as np
# UDP로 받기, 게이트웨이 통해서.
global intsain_illum
intsain_illum = np.zeros(10)

def set_illum_data(i, illum):
    global intsain_illum
    intsain_illum[i] = illum
    # print(intsain_illum[i])

def get_illum_data():
    global intsain_illum
    return intsain_illum
