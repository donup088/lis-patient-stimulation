import time

import pandas as pd

from hz_potential import potential, what_u_see


# from index_cal import int_to_index, time_str_to_int


def ssvep(idx, date):
    # print('ssvep')
    # print(idx)
    # print(date)
    time.sleep(20)  ######이거해놓으면 되나

    # 파일 실시간으로 받아오기
    # now = dt.datetime.now()
    # t_date = load_data.creat_Path(now)
    path = 'C:/MAVE_RawData/' + date + '/Rawdata.txt'
    raw = pd.read_csv(path, sep="\t", engine='python', encoding="cp949")
    # print('raw')
    # print(raw)

    fps = 210

    # 눈깜박임 감지 알려주기!-> 휴식 화면 ㄱㄱ
    # 30초동안
    blink_index = int(idx)  # 아무값
    ####################휴식 떄 7Hz, 13Hz
    # blink_time_str = raw.loc[blink_index, 'Time']
    # blink_time = time_str_to_int(blink_time_str)
    print("눈깜박임 순간")
    print(blink_index)
    # rest_start_index = int_to_index(raw.loc[:, 'Time'], blink_time + 9)
    rest_start_index = blink_index + 10 * fps
    # print(rest_start_index)
    # rest_end_index = int_to_index(raw.loc[:, 'Time'], blink_time + 29)
    rest_end_index = rest_start_index + 20 * fps
    # print(rest_end_index)
    # print("$$$$$$$$$$$$$$$")
    rest_7Hz, rest_13Hz = potential(raw, rest_start_index, rest_end_index)
    print("rest Hz")
    print(rest_7Hz, rest_13Hz)

    ##########################새로 읽고 자극때 7Hz, 13Hz
    stimul_start_index = len(raw) - 20 * fps
    # stimul_end_index = int_to_index(raw.loc[:, 'Time'], stimul_start_index + 20)
    stimul_end_index = len(raw)
    print("자극 끝 순간")
    print(len(raw))
    sti_7Hz, sti_13Hz = potential(raw, stimul_start_index, stimul_end_index)
    print("stimul Hz")
    print(sti_7Hz, sti_13Hz)
    ######################어떤 헤르츠의 전위 증가량이 더 큰가?
    see = what_u_see(rest_7Hz, rest_13Hz, sti_7Hz, sti_13Hz)

    return [see, len(raw)]
