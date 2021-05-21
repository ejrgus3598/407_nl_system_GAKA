# 색온도 센서 데이터 받고 API로도 보내고
import numpy as np
# rest 프로토콜 사용
global acs_cct
global acs_iluum

acs_cct = np.zeros(10)
acs_iluum = np.zeros(10)

def set_sensor_data(num, illum, cct):
    global acs_cct
    global acs_iluum

    acs_cct[num-1] = cct
    acs_iluum[num-1] = illum

def get_sensor_data():
    return [[acs_cct, acs_iluum]]