# 조도값 측정, DB에 누적

import numpy as np
# UDP로 받기, 게이트웨이 통해서.

class II:
    _instance = None
    def __init__(self):
        if not II._instance:
            self.intsain_illum = np.zeros(10)
            print('__init__ method called but nothing is created')
            # print([self.acs_cct, self.acs_illum])
        else:
            print('instance already created:', self.getInstance())
            # print([self.acs_cct, self.acs_illum])

    @classmethod
    def getInstance(cls):
        if not cls._instance:
            cls._instance = II()
        return cls._instance

    def set_illum_data(self, i, illum):
        self.intsain_illum[i] = illum
        # print(intsain_illum[i])

    def get_illum_data(self):
        return self.intsain_illum


