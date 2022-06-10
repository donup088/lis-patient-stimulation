import pandas as pd
import datetime as dt
import threading
import time
import os

now = dt.datetime.now()


def creat_Path(now):
    now = now
    t_month = ""
    t_day = ""
    t_minute = ""

    if now.month < 10:
        t_month = '0' + str(now.month)

    if now.day < 10:
        t_day = '0' + str(now.day)
    else:
        t_day = str(now.day)

    if now.minute < 10:
        t_minute = '0' + str(now.minute)
    else:
        t_minute = str(now.minute)

    t_hm = ""

    if now.hour > 12 and now.hour <= 23:
        t_hm = "오후 " + str(now.hour - 12) + '_' + str(t_minute)
    elif now.hour == 12:
        t_hm = "오후 " + str(now.hour) + '_' + str(t_minute)
    elif now.hour == 0:
        t_hm = "오전 " + str(now.hour + 12) + '_' + str(t_minute)
    else:
        t_hm = "오전 " + str(now.hour) + '_' + str(t_minute)

    t_date = str(now.year) + '-' + str(t_month) + '-' + str(t_day) + '_' + t_hm

    # print(t_date)
    return t_date


def loadRawdata(path):
    # print('raw thread')
    global raw_time
    global raw_value
    global raw
    try:
        #     path = 'C:/MAVE_RawData/2021-06-05_오후 5_18/Rawdata.txt'
        # path2 = 'C:/MAVE_RawData/오재무/2021-06-04_오후 5_52/Rawdata.txt'
        #     print(path)
        temp = pd.read_csv(path, delimiter='\t', encoding='cp949')
        # temp2 = pd.read_csv(path2,delimiter='\t',encoding='cp949')
        t_fp1 = temp['Time']
        e_fp1 = temp['EEG_Fp1']
        # t_fp2 = temp2['Time']
        # e_fp2 = temp2['EEG_Fp1']

        raw_time = t_fp1
        raw_value = e_fp1
        raw = temp

    except TypeError:
        print("지정된 경로에 파일이 없습니다.")
        pass
