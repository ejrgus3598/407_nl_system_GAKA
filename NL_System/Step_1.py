# 암막, 자연광 색온도, 실시간, cas, 필요조도, 색온도 재현
import pandas as pd
from MongoDB import Load_MongoDB as LMDB
from NL_System import Base_Process as bp
from Core import Intsain_LED as ILED
import numpy as np
import threading, time
from Core.arduino_color_sensor import acs
from Core.Intsain_Illum import II
from Core.Intsain_Curr import IC

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]

def load_NL_CCT_mongo():
    step_data = LMDB.load_last1_cct()
    step_df = LMDB.mongodb_to_df(step_data, 'mongo_cas')
    step_df = step_df.reset_index(drop=True)
    return step_df

def process():
    # 센싱부 실행
    base = threading.Thread(target=bp.process)
    base.start()

    # 기준 조도, 색온도 설정
    target_illum = 200
    mongo_df = load_NL_CCT_mongo()
    cct_now = float(mongo_df['CCT'].values[0])
    cct_now = 2700
    print(cct_now)

    # 제어지표 필터링.
    control_pd = pd.read_csv("../LEDcontrol_list.csv")
    control_pd["illum"] = control_pd["illum"].astype(float)
    control_pd["cct"] = control_pd["cct"].astype(float)

    mask = (control_pd.illum >= target_illum-50) & (control_pd.illum <= target_illum+50) & (control_pd.cct >= cct_now-100) & (control_pd.cct <= cct_now+100)
    print(control_pd[mask][['idx','ch.1','ch.2','ch.3','ch.4','illum','cct']])
    temp = control_pd[mask]['cct'].values
    temp_df = control_pd[mask]
    temp_df = temp_df.reset_index(drop=True)
    target_cct = find_nearest(temp, cct_now)
    final_df = temp_df[temp_df['cct']==target_cct]
    ch1 = int(final_df['ch.1'].values[0])
    ch2 = int(final_df['ch.2'].values[0])
    ch3 = int(final_df['ch.3'].values[0])
    ch4 = int(final_df['ch.4'].values[0])

    ILED.all_set_LED(ch1,ch2,ch3,ch4)

    time.sleep(10)


if __name__ == '__main__':
    process()