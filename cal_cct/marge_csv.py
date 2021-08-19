import pandas as pd

def process():
    ori_path = "D:\\BunkerBuster\\Desktop\\보정자료\\"

    cct_df = pd.read_csv(ori_path+"cct.csv")
    illum_df = pd.read_csv(ori_path+"illum.csv")
    log_df = pd.read_csv(ori_path+"log_jaz.csv")

    log_df['jaz_cct'] = log_df.apply(lambda x: 0, axis=1)
    log_df['jaz_illum'] = log_df.apply(lambda x: 0, axis=1)

    for i in range(len(log_df)):
        flag_time = float(log_df.loc[i,"Timestamp"])
        for j in range(len(cct_df)-1):
            cct_time_1 = float(cct_df.loc[j, "Timestamp"])
            cct_time_2 = float(cct_df.loc[j+1, "Timestamp"])
            if cct_time_1<=flag_time:
                if flag_time <cct_time_2:
                    log_df.loc[i, "jaz_cct"] = cct_df.loc[j, "CCT"]
                    print("색온도",i)
                    break

        # for j in range(len(illum_df)-1):
        #     illum_time_1 = float(illum_df.loc[j, "Timestamp"])
        #     illum_time_2 = float(illum_df.loc[j+1, "Timestamp"])
        #     if illum_time_1<flag_time:
        #         if flag_time <illum_time_2:
        #             log_df.loc[i, "jaz_illum"] = illum_df.loc[j, "illum"]
        #             print("조도",i)
        #             break

    log_df.to_csv(ori_path+"marge.csv")
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import pandas as pd
from string import ascii_uppercase


# import my data
def process2():
    ori_path = "D:\\BunkerBuster\\Desktop\\보정자료\\"
    df = pd.read_csv(ori_path + "marge.csv")
    for i in range(1,10):
        temp = df[df['task_type']=="diff_test_point_"+str(i)]
        temp = temp[["task_type","cct_"+str(i), "jaz_cct"]]
        temp.to_csv("diff_test_point_"+str(i)+".csv")


        xdata = temp["cct_"+str(i)]
        ydata = temp["jaz_cct"]

        # define polynomial function
        def func(X, A, B):
            # unpacking the multi-dim. array column-wise, that's why the transpose
            x = X
            return (A * x) + B
        # fit the polynomial function to the 3d data
        popt, _ = curve_fit(func, xdata, ydata)

        # print coefficients of the polynomial function, i.e., A, B, C, D, E and F
        print(str(i)+"번 센서 보정식 : ")
        for a, b in zip(popt, ascii_uppercase):
            print(f"{b} = {a:.10f}")



if __name__ == '__main__':
    # process()
    process2()
