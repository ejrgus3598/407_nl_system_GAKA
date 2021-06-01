# 암막, 자연광 색온도, 실시간, cas, 필요조도, 색온도 재현
import pandas as pd
from multiprocessing import Process, Queue
from MongoDB import Load_MongoDB as LMDB
from NL_System import Base_Process as bp
from Core import Intsain_LED as ILED
import numpy as np
from Core import Intsain_Curr as IC
from Core import Intsain_Illum as II
from Core import arduino_color_sensor as acs





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
    # base = Process(target=bp.process)
    # base.start()

    target_illum = 200
    # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(II.get_illum_data())

    mongo_df = load_NL_CCT_mongo()
    cct_now = float(mongo_df['CCT'].values[0])
    print(cct_now)

    control_pd = pd.read_csv("../LEDcontrol_list.csv")
    # print(control_pd)
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
    print(II.get_illum_data())



if __name__ == '__main__':
    process()