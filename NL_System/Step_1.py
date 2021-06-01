# 암막, 자연광 색온도, 실시간, cas, 필요조도, 색온도 재현
import pandas as pd
from multiprocessing import Process, Queue
from MongoDB import Load_MongoDB as LMDB
from NL_System import Base_Process as bp


def load_NL_CCT_mongo():
    step_data = LMDB.load_last1_cct()
    step_df = LMDB.mongodb_to_df(step_data, 'mongo_cas')
    step_df = step_df.reset_index(drop=True)
    return step_df

def process():
    base = Process(target=bp.process)
    base.start()

    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    mongo_df = load_NL_CCT_mongo()
    cct_now = mongo_df['CCT'].values[0]
    print(cct_now)


if __name__ == '__main__':
    process()