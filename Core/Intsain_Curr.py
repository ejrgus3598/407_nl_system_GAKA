# 전력량 측정, DB에 누적
import numpy as np
# UDP로 받기, 게이트웨이 통해서.
global intsain_curr
intsain_curr = np.zeros(10)

def set_curr_data(currs):
    # global intsain_curr

    intsain_curr = currs
