from datetime import datetime

import pandas as pd

import Shin_Package.open_processor_0_1.datas as datas

# 스텝별로 제어 상태, 센서 값 저장하는 함수
def save_data(start, acs_cct, II_illum, IC_curr, avg_cct, avg_illum, sum_curr, uniformity, get_times,
              save_name,
              isPrint):
    df_record=[]
    step_end = datetime.now()
    led_num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
                    25, 26, 27, 28, 29, 30]
    df_record.append(pd.DataFrame(led_num_list, columns=['led']))
    for idx in range(1, len(datas.led_state)):
        df_record[len(df_record) - 1].loc[idx - 1, 'control'] = datas.led_control_lux[datas.led_state[idx]]
        if (idx < 10):
            df_record[len(df_record) - 1].loc[idx - 1, 'cct'] = acs_cct[idx - 1]
            df_record[len(df_record) - 1].loc[idx - 1, 'illum'] = II_illum[idx - 1]
            df_record[len(df_record) - 1].loc[idx - 1, 'curr'] = IC_curr[idx - 1]
            df_record[len(df_record) - 1].loc[idx - 1, 'natural_light'] = datas.illum_add[idx - 1]
        elif (idx < 11):
            df_record[len(df_record) - 1].loc[idx - 1, 'curr'] = IC_curr[idx - 1]
    df_record[len(df_record) - 1].loc[10, 'cct'] = avg_cct
    df_record[len(df_record) - 1].loc[10, 'illum'] = avg_illum
    df_record[len(df_record) - 1].loc[10, 'curr'] = sum_curr
    df_record[len(df_record) - 1].loc[0, 'uniformity'] = uniformity
    df_record[len(df_record) - 1].loc[0, 'start'] = start
    df_record[len(df_record) - 1].loc[0, 'end'] = step_end
    df_record[len(df_record) - 1].loc[0, 'diff_time'] = step_end - start

    for i in range(len(datas.illum_change_time)):
        df_record[len(df_record) - 1].loc[i, 'illum_change_time'] = datas.illum_change_time[i]

    if (isPrint):
        print('=' * 20)
        # print(df_record[len(df_record) - 1])
        print('====save_success====')
        print('=' * 20)

    df_record[len(df_record) - 1].to_csv(
        "D:\\BunkerBuster\\Desktop\\shin_excel\\24시작\\new_index\\%s\\[%s]_step%s.csv" % (
            datas.save_folder, get_times - 1, save_name))
    print(start, "->", step_end)

def print_all():
    # 현재 데이터 상태 출력
    print_control_lux()
    print_led_locking_state(datas.led_up_lock, "UP")
    print_led_locking_state(datas.led_down_lock, "DOWN")
    print_sensor_locking_state()
    print_natural_light_state()

# 현재 컨트롤 lux 상태 출력
def print_control_lux():
    print("Control Lux")
    for idx in range(1, len(datas.led_state)):
        print("%s\t" % datas.led_control_lux[datas.led_state[idx]], end='')
        if idx % 6 == 0:
            print()

    # print("LED state")
    # for idx in range(1, len(led_state)):
    #     print("%s\t" % led_state[idx], end='')
    #     if idx % 6 == 0:
    #         print()


# 현재 조명 잠금 상태 출력
def print_led_locking_state(led_lock, mode):
    print("LED Locking State [%s]" % mode)
    for idx in range(1, len(led_lock)):
        print("%s\t" % led_lock[idx], end='')
        if idx % 6 == 0:
            print()


# 현재 센서 잠금 상태 출력
def print_sensor_locking_state():
    print("Sensor Up Locking State")
    for idx in range(len(datas.sensor_up_lock)):
        print("%s\t" % datas.sensor_up_lock[idx], end='')
        if idx % 3 == 2:
            print()
    print("Sensor Down Locking State")
    for idx in range(len(datas.sensor_down_lock)):
        print("%s\t" % datas.sensor_down_lock[idx], end='')
        if idx % 3 == 2:
            print()


def print_natural_light_state():
    print("Virtual Natural Light")
    for i in range(len(datas.illum_add)):
        print(datas.illum_add[i], ' ', end='')
        if (i % 3 == 2):
            print()