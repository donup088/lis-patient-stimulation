import numpy as np
import pandas as pd
import datetime as dt

import time
import load_data
import FindBlink


def analysis():
    print('함수 실행')
    # 파일 실시간으로 받아오기
    now = dt.datetime.now()
    t_date = load_data.creat_Path(now)
    path = 'C:/MAVE_RawData/' + t_date
    print(path)
    load_data.loadRawdata(path)

    path_raw = 'C:/MAVE_RawData/2022-06-10_오후 2_29/Biomarkers.txt'  # 파일 경로
    path_bio = path + '/Biomarkers.txt'

    while (1):
        bio = pd.read_csv(path_raw, sep="\t", engine='python', encoding="cp949")
        theta = bio.loc[:, 'Fp1_Theta(%)']
        if FindBlink.find_blink(theta) != 0:
            blink_index = FindBlink.find_blink(theta)
            break

    # 눈깜박임 감지 알려주기!-> 휴식 화면 ㄱㄱ
    # 30초동안
    time.sleep(10)
    while 1:
        raw = pd.read_csv(path_raw, sep="\t", engine='python', encoding="cp949")
