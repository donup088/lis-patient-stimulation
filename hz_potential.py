import preprocessing


def potential(raw, index_s, index_e):
    print('po')
    fs = (index_e - index_s)/20
    raw_ = raw.loc[:, ['EEG_Fp1', 'EEG_Fp2']]
    print("raw")
    print(raw)
    print(raw.shape)
    pre = preprocessing.butter_bandpass_filter(raw_, 1, 30, fs)
    eeg = preprocessing.ica(pre, 2)
    eeg_n = eeg[1]
    fp1_ssvep = eeg_n[index_s:index_e * fs, 0]  # 시작 시점 인덱스
    Hz7_fp1, Hz13_fp1 = preprocessing.analysis_ssvep(fp1_ssvep, fs, 6.6, 7)
    return Hz7_fp1, Hz13_fp1


def what_u_see(r_7, r_13, sti_7, sti_13):
    diff_7 = sti_7 - r_7
    diff_13 = sti_13 - r_13
    print('see')
    print(diff_7, diff_13)
    if diff_7 - diff_13 > 0:
        return 6.6  # 7변화가 더 크다
    else:
        return 7  # 13변화가 더 크다

#
# def potential_compare(raw,index_s, fs=250):
#     pre = preprocessing.butter_bandpass_filter(raw, 1, 30, fs)
#     eeg = preprocessing.ica(pre, 2)
#     eeg_n = eeg[1]
#     fp1_ssvep = eeg_n[index_s:, 0]  # 시작 시점 인덱스
#     Hz7_fp1, Hz13_fp1 = preprocessing.analysis_ssvep(fp1_ssvep, fs, 7, 13)
